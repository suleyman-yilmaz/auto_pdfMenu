# EN - auto_pdfMenu

**auto_pdfMenu** is a Flask-based web application and offers different PDF files depending on the time available. The project includes QR code generation to provide easy access to PDF documents.


# Features

- Time Based PDF Display:** Shows different PDF files before and after 12:00.
- QR Code Generation:** Generates a QR code that links to the PDF viewer.
- Direct PDF Viewing:** Opens PDFs directly in the browser, no download.

## Getting Started

Follow the steps below to start this project:

#### Requirements

- Python 3.12
- Flask
- qrcode (Python library for generating QR codes)

## Installation

1. **Clone the Warehouse**
```bash
 git clone https://github.com/suleyman-yilmaz/auto_pdfMenu.git
```

2. **Load Addictions**
- pip install Flask
- pip install DateTime
- pip install qrcode

3. **Run the App**
- python app.py

  The application will be available at \`http://localhost:5000/menu`.


## Usage

- **Access to PDF Viewer:**
  - In the generate_qr.py file, you need to edit the url according to the IPv4 Address of your computer. Access is provided only when the qr code is scanned from the phone after entering the IPv4 Address. 
  - You can scan the generated QR code with your phone and view the PDF depending on the time available.
  - Alternatively, you can visit \`http://localhost:5000/menu` to test the application.

## File Structure

- \``app.py\`: Main Flask application file.
- \``generate_qr.py\`: Script to generate the QR code.
- \``static/\`: Directory with PDF files (\``morning.pdf\`, \`afternoon.pdf\`).


## Contributing

We look forward to your contributions! If you find problems or have suggestions for improvement, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Thank you

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [qrcode](https://pypi.org/project/qrcode/)


# TR - auto_pdfMenu

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
```bash
 git clone https://github.com/suleyman-yilmaz/auto_pdfMenu.git
```

2. **Bağımlılıkları Yükleyin**
-	pip install Flask
-	pip install DateTime
-	pip install qrcode

3. **Uygulamayı Çalıştırın**
- python app.py

  Uygulama \`http://localhost:5000/menu` adresinde kullanılabilir olacaktır.


## Kullanım

- **PDF Görüntüleyiciye Erişim:**
  - generate_qr.py dosyasında url'yi bilgisayarınızın IPv4 Adress ine göre düzenlemeniz gerekmektedir. Sadece IPv4 Adressi ni girdikten sonra telefondan qr kodu okutulduğunda erişim sağlanmaktadır. 
  - Oluşturulan QR kodunu telefonunuzla tarayarak mevcut zamana bağlı olarak PDF'yi görüntüleyebilirsiniz.
  - Alternatif olarak, uygulamayı test etmek için \`http://localhost:5000/menu` adresini ziyaret edebilirsiniz.

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
