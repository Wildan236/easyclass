from flask import Flask, render_template, Response
from datetime import datetime
from module import database_module

app = Flask(__name__)

# bikin/ generate data siswa
def get_siswa_data():
    siswa = [['absen', 'Nama','NIS', 'Masuk', 'Keluar']]
    for sis in database_module.siswa:
        siswa.append([sis['absen'] ,sis['nama'], sis['nis'], sis['masuk'], sis['keluar']])
    return siswa

# yang menulis waktu saat tap
def time_writer(id):
    waktu_sekarang = datetime.now()
    
    # sekarang jam berapa
    jam = waktu_sekarang.hour
    waktu_sekarang = waktu_sekarang.strftime("%H:%M:%S") # ini jangan dihapus, ini untuk menampilkan di web
    
    #mendapatkan semua id siswa 
    id_siswa = []
    for sis in database_module.siswa:
        id_siswa.append(sis['id'])
    
    #mencocokan id rfid yang baru saja terbaca ke id siswa
    for id_index in range(len(id_siswa)):
        if id == id_siswa[id_index]:
            #jadwal jam masuk jam berapa
            # jika kurang dari jam 8 maka dianggap masuk
            if jam < 7 :
                # disini codingan masuk
                if database_module.siswa[id_index]['masuk'] == 0:
                    database_module.siswa[id_index]['masuk'] = waktu_sekarang
                else:
                    print('sudah absen')
                break
            
            # jika lebih dari dari jam 16 maka dianggap pulang
            elif jam > 16 :
                if database_module.siswa[id_index]['keluar'] == 0:
                    database_module.siswa[id_index]['keluar'] = waktu_sekarang
                else:
                    print("sudah keluar")
                break

@app.route('/')
def index():
    siswa = get_siswa_data()
    return render_template('index.html', murid=siswa)

# cara memakainya
# if __name__ == '__main__':
#     app.run(host='0.0.0.0')