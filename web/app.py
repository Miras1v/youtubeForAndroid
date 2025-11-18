from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import yt_dlp
import os
import re
import requests
from pathlib import Path
import tempfile
import json

app = Flask(__name__)
CORS(app)

# İndirme klasörü
DOWNLOAD_DIR = Path('downloads')
DOWNLOAD_DIR.mkdir(exist_ok=True)

# YouTube Data API v3 için (opsiyonel - arama için)
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')


def extract_video_id(url):
    """YouTube URL'den video ID çıkarır"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_video_info(url):
    """Video bilgilerini alır"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'Bilinmeyen'),
                'thumbnail': info.get('thumbnail', ''),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', ''),
                'view_count': info.get('view_count', 0),
                'formats': []
            }
    except Exception as e:
        return {'error': str(e)}


def download_video(url, format_type='video'):
    """Video veya ses indirir"""
    output_path = DOWNLOAD_DIR / '%(title)s.%(ext)s'
    
    if format_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(output_path),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': str(output_path),
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Ses indiriyorsak .mp3 uzantısını ekle
            if format_type == 'audio':
                filename = filename.rsplit('.', 1)[0] + '.mp3'
            
            return {
                'success': True,
                'filename': os.path.basename(filename),
                'filepath': filename,
                'title': info.get('title', 'Bilinmeyen')
            }
    except Exception as e:
        return {'success': False, 'error': str(e)}


def search_youtube(query, max_results=10):
    """YouTube'da arama yapar"""
    if not YOUTUBE_API_KEY:
        # API key yoksa yt-dlp ile arama yap
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,
            }
            search_url = f'ytsearch{max_results}:{query}'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                results = []
                info = ydl.extract_info(search_url, download=False)
                if 'entries' in info:
                    for entry in info['entries']:
                        if entry:
                            results.append({
                                'video_id': entry.get('id', ''),
                                'title': entry.get('title', 'Bilinmeyen'),
                                'url': f"https://www.youtube.com/watch?v={entry.get('id', '')}",
                                'duration': entry.get('duration', 0),
                                'thumbnail': f"https://img.youtube.com/vi/{entry.get('id', '')}/default.jpg"
                            })
                return results
        except Exception as e:
            return {'error': str(e)}
    else:
        # YouTube Data API v3 kullan
        try:
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': max_results,
                'key': YOUTUBE_API_KEY
            }
            response = requests.get(search_url, params=params)
            data = response.json()
            
            results = []
            for item in data.get('items', []):
                video_id = item['id']['videoId']
                results.append({
                    'video_id': video_id,
                    'title': item['snippet']['title'],
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'thumbnail': item['snippet']['thumbnails']['default']['url'],
                    'channel': item['snippet']['channelTitle'],
                    'description': item['snippet']['description']
                })
            return results
        except Exception as e:
            return {'error': str(e)}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/info', methods=['POST'])
def get_info():
    """Video bilgilerini döndürür"""
    data = request.json
    url = data.get('url', '')
    
    if not url:
        return jsonify({'error': 'URL gerekli'}), 400
    
    info = get_video_info(url)
    return jsonify(info)


@app.route('/api/download', methods=['POST'])
def download():
    """Video veya ses indirir"""
    data = request.json
    url = data.get('url', '')
    format_type = data.get('format', 'video')  # 'video' veya 'audio'
    
    if not url:
        return jsonify({'error': 'URL gerekli'}), 400
    
    result = download_video(url, format_type)
    
    if result.get('success'):
        return jsonify({
            'success': True,
            'filename': result['filename'],
            'title': result['title'],
            'download_url': f"/api/file/{result['filename']}"
        })
    else:
        return jsonify({'success': False, 'error': result.get('error', 'Bilinmeyen hata')}), 500


@app.route('/api/search', methods=['POST'])
def search():
    """YouTube'da arama yapar"""
    data = request.json
    query = data.get('query', '')
    max_results = data.get('max_results', 10)
    
    if not query:
        return jsonify({'error': 'Arama terimi gerekli'}), 400
    
    results = search_youtube(query, max_results)
    
    if isinstance(results, dict) and 'error' in results:
        return jsonify(results), 500
    
    return jsonify({'results': results})


@app.route('/api/file/<filename>')
def download_file(filename):
    """İndirilen dosyayı sunar ve tarayıcıya gönderir"""
    filepath = DOWNLOAD_DIR / filename
    if filepath.exists():
        # Dosyayı tarayıcıya gönder ve sonra sil
        response = send_file(str(filepath), as_attachment=True, download_name=filename)
        # Dosyayı arka planda sil (async olarak)
        import threading
        def delete_file():
            import time
            time.sleep(1)  # İndirme tamamlanması için bekle
            try:
                if filepath.exists():
                    filepath.unlink()
            except:
                pass
        threading.Thread(target=delete_file, daemon=True).start()
        return response
    return jsonify({'error': 'Dosya bulunamadı'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

