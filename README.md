# 🎬 YouTube İndirici - Web ve Android

YouTube'dan video ve ses dosyalarını indirmek için web ve Android uygulaması.

## 📁 Proje Yapısı

```
youtubeForAndroid/
├── web/                           # Web uygulaması (Flask)
│   ├── app.py                    # Flask backend
│   ├── requirements.txt          # Python bağımlılıkları
│   ├── templates/                # HTML şablonları
│   │   └── index.html
│   └── README.md                 # Web uygulaması dokümantasyonu
├── android/                      # Android uygulaması (React Native)
│   ├── App.js                   # Ana uygulama bileşeni
│   ├── package.json             # Node.js bağımlılıkları
│   ├── app/                     # Android native dosyalar
│   │   └── src/
│   │       └── main/
│   │           └── AndroidManifest.xml
│   └── README.md                # Android uygulaması dokümantasyonu
└── README.md                    # Bu dosya
```

## ✨ Özellikler

### Web Uygulaması
- 🔗 **Link ile İndirme**: YouTube URL'sini yapıştırarak hızlıca indirme
- 🔍 **Arama Özelliği**: Uygulama içinden YouTube'da arama yapma
- 📹 **Video İndirme**: Yüksek kaliteli video indirme
- 🎵 **Ses İndirme**: MP3 formatında ses dosyası indirme
- 📱 **Mobil Uyumlu**: Tüm cihazlarda çalışır

### Android Uygulaması
- 🔗 **Link ile İndirme**: YouTube URL'sini yapıştırarak hızlıca indirme
- 🔍 **Arama Özelliği**: Uygulama içinden YouTube'da arama yapma
- 📹 **Video İndirme**: Yüksek kaliteli video indirme
- 🎵 **Ses İndirme**: MP3 formatında ses dosyası indirme
- 📱 **Native Android**: React Native ile geliştirilmiş

## 🚀 Hızlı Başlangıç

### Web Uygulaması

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

### Android Uygulaması

1. **Backend'i çalıştırın** (yukarıdaki adımlar)

2. **IP adresinizi bulun**
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` veya `ip addr`

3. **Android uygulamasını yapılandırın**
   - `android/App.js` dosyasındaki `API_URL` değişkenini kendi IP adresinizle değiştirin:
   ```javascript
   const API_URL = 'http://192.168.1.100:5000'; // Kendi IP adresinizi girin
   ```

4. **Bağımlılıkları yükleyin**
```bash
cd youtubeForAndroid/android
npm install
```

5. **Android uygulamasını çalıştırın**
```bash
npm run android
```

## 📋 Gereksinimler

### Web Uygulaması
- Python 3.8+
- FFmpeg (ses dönüştürme için)

### Android Uygulaması
- Node.js 16+
- React Native CLI
- Android Studio
- Java JDK 11+
- Backend API çalışıyor olmalı

## 📖 Detaylı Dokümantasyon

- **Web Uygulaması**: [web/README.md](web/README.md)
- **Android Uygulaması**: [android/README.md](android/README.md)

## ⚙️ Yapılandırma

### Backend API URL (Android için)

Android uygulaması, web uygulamasına bağlanır. `android/App.js` dosyasındaki `API_URL` değişkenini kendi IP adresinizle değiştirin:

```javascript
const API_URL = 'http://192.168.1.100:5000'; // Kendi IP adresinizi girin
```

**Önemli:** Telefon ve bilgisayar aynı ağda olmalıdır.

### YouTube API Key (Opsiyonel)

Arama özelliği için YouTube Data API v3 kullanmak isterseniz:

1. [Google Cloud Console](https://console.cloud.google.com/) hesabı oluşturun
2. YouTube Data API v3'ü etkinleştirin
3. API key oluşturun
4. `.env` dosyası oluşturun (web klasöründe):
```env
YOUTUBE_API_KEY=your-api-key-here
```

**Not:** API key olmadan da arama çalışır (yt-dlp kullanır), ancak API key ile daha hızlı ve güvenilir sonuçlar alırsınız.

## 🐛 Sorun Giderme

### Web Uygulaması

**FFmpeg Hatası:**
- FFmpeg'in PATH'te olduğundan emin olun
- FFmpeg kurulumunu kontrol edin

**İndirme Hatası:**
- Video URL'sinin doğru olduğundan emin olun
- İnternet bağlantınızı kontrol edin

### Android Uygulaması

**Backend'e Bağlanamıyor:**
- Backend'in çalıştığından emin olun
- IP adresinin doğru olduğundan emin olun
- Telefon ve bilgisayarın aynı ağda olduğundan emin olun
- Firewall'ın 5000 portunu engellemediğinden emin olun

**İndirme Çalışmıyor:**
- Depolama izninin verildiğinden emin olun
- Yeterli depolama alanı olduğundan emin olun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

