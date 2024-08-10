# auto_pdfMenu

**auto_pdfMenu** bir Flask tabanlı web uygulamasıdır ve mevcut zamana bağlı olarak farklı PDF dosyaları sunar. Proje, PDF belgelerine kolay erişim sağlamak için QR kodu üretimini içerir.


# Özellikler

- **Zamana Dayalı PDF Gösterimi:** Saat 12:00'den önce ve sonra farklı PDF dosyalarını gösterir.
- **QR Kod Oluşturma:** PDF görüntüleyiciye bağlanan bir QR kodu oluşturur.
- **Doğrudan PDF Görüntüleme:** PDF'leri tarayıcıda doğrudan açar, indirme işlemi yapmaz.

## Başlarken

Bu projeye başlamak için aşağıdaki adımları izleyin:

### Gereksinimler

- Python 3.12
- Flask
- qrcode (QR kodları oluşturmak için Python kütüphanesi)

## Kurulum

1. **Depoyu Klonlayın**
- git clone https://github.com/suleyman-yilmaz/auto_pdfMenu.git
- cd auto_pdfMenu


2. **Bağımlılıkları Yükleyin**
-	pip install Flask
-	pip install DateTime
-	pip install qrcode

3. **Uygulamayı Çalıştırın**
- python generate_pdf.py
- python app.py

  Uygulama \`http://localhost:5000/menu` adresinde kullanılabilir olacaktır.


## Kullanım

- **PDF Görüntüleyiciye Erişim:**
  - Oluşturulan QR kodunu telefonunuzla tarayarak mevcut zamana bağlı olarak PDF'yi görüntüleyebilirsiniz.
  - Alternatif olarak, uygulamayı test etmek için \`http://localhost:5000/menu\` adresini ziyaret edebilirsiniz.

## Dosya Yapısı

- \`app.py\`: Ana Flask uygulama dosyası.
- \`generate_qr.py\`: QR kodunu oluşturma betiği.
- \`static/\`: PDF dosyalarının bulunduğu dizin (\`morning.pdf\`, \`afternoon.pdf\`).


## Katkıda Bulunma

Katkılarınızı bekliyoruz! Sorun bulursanız veya iyileştirme önerileriniz varsa, lütfen bir pull request gönderin veya bir sorun açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.

## Teşekkürler

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [qrcode](https://pypi.org/project/qrcode/)
