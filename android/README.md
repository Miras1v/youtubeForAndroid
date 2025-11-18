# 📱 YouTube İndirici - Android

YouTube'dan video ve ses dosyalarını indirmek için Android uygulaması.

## ✨ Özellikler

- 🔗 **Link ile İndirme**: YouTube URL'sini yapıştırarak hızlıca indirme
- 🔍 **Arama Özelliği**: Uygulama içinden YouTube'da arama yapma
- 📹 **Video İndirme**: Yüksek kaliteli video indirme
- 🎵 **Ses İndirme**: MP3 formatında ses dosyası indirme
- 📱 **Native Android**: React Native ile geliştirilmiş

## 🚀 Kurulum

### Gereksinimler

- Node.js 16+
- React Native CLI
- Android Studio
- Java JDK 11+
- Backend API çalışıyor olmalı (web klasöründeki Flask uygulaması)

### Adımlar

1. **Backend'i çalıştırın**

Başka bir terminalde:
```bash
cd ../web
pip install -r requirements.txt
python app.py
```

2. **IP adresinizi bulun**

- Windows: `ipconfig` komutunu çalıştırın
- Mac/Linux: `ifconfig` veya `ip addr` komutunu çalıştırın

3. **Android uygulamasını yapılandırın**

`App.js` dosyasındaki `API_URL` değişkenini kendi IP adresinizle değiştirin:
```javascript
const API_URL = 'http://192.168.1.100:5000'; // Kendi IP adresinizi girin
```

4. **Bağımlılıkları yükleyin**
```bash
cd android
npm install
```

5. **Android uygulamasını çalıştırın**
```bash
npm run android
```

## 📖 Kullanım

### Link ile İndirme

1. "Link" sekmesine gidin
2. YouTube video URL'sini yapıştırın
3. "Video Bilgilerini Getir" butonuna tıklayın
4. "Video İndir" veya "Ses İndir (MP3)" butonuna tıklayın
5. Dosya İndirilenler klasörüne kaydedilir

### Arama ile İndirme

1. "Arama" sekmesine gidin
2. Arama terimini girin
3. "Ara" butonuna tıklayın
4. Sonuçlardan bir videoya tıklayın
5. Otomatik olarak link sekmesine geçer
6. İndirme butonlarına tıklayın

## ⚙️ Yapılandırma

### İzinler

Uygulama aşağıdaki izinleri gerektirir:
- İnternet erişimi
- Depolama erişimi (dosya indirme için)

### Backend Bağlantısı

Uygulama, backend API'ye HTTP üzerinden bağlanır. Aynı ağda olmanız gerekir.

## 🐛 Sorun Giderme

### Backend'e Bağlanamıyor

- Backend'in çalıştığından emin olun
- IP adresinin doğru olduğundan emin olun
- Telefon ve bilgisayarın aynı ağda olduğundan emin olun
- Firewall'ın 5000 portunu engellemediğinden emin olun

### İndirme Çalışmıyor

- Depolama izninin verildiğinden emin olun
- Yeterli depolama alanı olduğundan emin olun
- İnternet bağlantınızı kontrol edin

### Build Hatası

- `npm install` komutunu tekrar çalıştırın
- `cd android && ./gradlew clean` komutunu çalıştırın
- Node.js ve React Native versiyonlarını kontrol edin

## 📝 Notlar

- Bu uygulama, backend API'ye bağımlıdır
- Backend API çalışmıyorsa uygulama çalışmaz
- İndirilen dosyalar İndirilenler klasörüne kaydedilir

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

