from flask import Flask, render_template, Response
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    masuk = datetime.now().date()
    keluar = datetime.now().date()
    user = [['Nama', 'Masuk', 'Keluar']]
    user.append(['Didik', masuk, keluar])
    user.append(['Paijo', masuk, keluar])
    return render_template('index.html', murid=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)