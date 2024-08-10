from flask import Flask, send_file, Response
from datetime import datetime

app = Flask(__name__)

@app.route('/menu')
def get_menu():
    current_time = datetime.now().time()
    if current_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        pdf_file = 'static/morning.pdf'
    else:
        pdf_file = 'static/afternoon.pdf'

    # PDF'yi inline olarak tarayıcıda açmak için
    response = send_file(pdf_file, as_attachment=False, mimetype='application/pdf')
    response.headers["Content-Disposition"] = "inline; filename={}".format(pdf_file.split('/')[-1])
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')