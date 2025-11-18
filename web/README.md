# 🎬 YouTube İndirici - Web Uygulaması

YouTube'dan video ve ses dosyalarını indirmek için web uygulaması.

## ✨ Özellikler

- 🔗 **Link ile İndirme**: YouTube URL'sini yapıştırarak hızlıca indirme
- 🔍 **Arama Özelliği**: Uygulama içinden YouTube'da arama yapma
- 📹 **Video İndirme**: Yüksek kaliteli video indirme
- 🎵 **Ses İndirme**: MP3 formatında ses dosyası indirme
- 📱 **Mobil Uyumlu**: Tüm cihazlarda çalışır

## 🚀 Kurulum

### Gereksinimler

- Python 3.8+
- FFmpeg (ses dönüştürme için)

### FFmpeg Kurulumu

**Windows:**
1. [FFmpeg indir](https://ffmpeg.org/download.html)
2. ZIP dosyasını çıkarın
3. `bin` klasörünü PATH'e ekleyin

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### Adımlar

1. **Bağımlılıkları yükleyin**
```bash
cd youtubeForAndroid/web
pip install -r requirements.txt
```

2. **Uygulamayı çalıştırın**
```bash
python app.py
```

3. **Tarayıcıda açın**
```
http://localhost:5000
```

## 📖 Kullanım

### Link ile İndirme

1. "Link ile İndir" sekmesine gidin
2. YouTube video URL'sini yapıştırın
3. "Video Bilgilerini Getir" ile önizleme yapın
4. "Video İndir" veya "Ses İndir (MP3)" butonuna tıklayın

### Arama ile İndirme

1. "Arama Yap" sekmesine gidin
2. Arama terimini girin
3. Sonuçlardan bir videoya tıklayın
4. Otomatik olarak link sekmesine geçer ve video bilgileri yüklenir
5. İndirme butonlarına tıklayın

## ⚙️ Opsiyonel: YouTube API Key

Arama özelliği için YouTube Data API v3 kullanmak isterseniz:

1. [Google Cloud Console](https://console.cloud.google.com/) hesabı oluşturun
2. YouTube Data API v3'ü etkinleştirin
3. API key oluşturun
4. `.env` dosyası oluşturun:
```env
YOUTUBE_API_KEY=your-api-key-here
```

**Not:** API key olmadan da arama çalışır (yt-dlp kullanır), ancak API key ile daha hızlı ve güvenilir sonuçlar alırsınız.

## 📁 İndirilen Dosyalar

İndirilen dosyalar `downloads/` klasörüne kaydedilir.

## 🐛 Sorun Giderme

### FFmpeg Hatası

Ses indirme için FFmpeg gereklidir. FFmpeg'in PATH'te olduğundan emin olun.

### İndirme Hatası

- Video URL'sinin doğru olduğundan emin olun
- İnternet bağlantınızı kontrol edin
- Video erişilebilir olduğundan emin olun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

