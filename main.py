#import semua module

#import module led
from module.lampu_module import *

#import module RFID
from module.rfid_module import *

#import module suhu
from module.suhu_module import *

#import module ubidots
from module.ubidots_module import * 

#import module web
from module.web_module import *

#import module bot telegram
from module.telegram_module import *

import time
import threading

'''
main
# bagian suhu
1. deteksi sensor suhu
2. kirim data suhu ke ubidots

# bagian lampu
1. menerima daata lampu & led dari ubidots
2. nyalakam, matikan lampu & led lewat ubidots

#bagian rfid
1. bikin web

#tambahan
1. bikin notifikasi lewat bot tele saat suhu & kelembaban melebihi batas normal
'''

def main(_):
    while(1):
        humidity, temperature = get_sensor_suhu_data()
        kirim_suhu(humidity, temperature)

        lampu_state = menerima_data_lampu()
        ac_state = menerima_data_ac()
        tv_state = menerima_data_tv()

        lampu(lampu_state)
        ac(ac_state)
        tv(tv_state)

        if temperature < 30 :
            send_to_telegram("Sensor suhu mendeteksi Temperature dan Kelembaban yang tidak nomal, SEGERA PERIKSA APLIKASI!!!")
            
def loop_baca_rfid(_):
    while(1):
        id, nama = baca_rfid()
        time_writer(id)
        time.sleep(0.1)

# bikin thread untuk membaca RFID agar bisa loop terus
rfid_thread = threading.Thread(target=loop_baca_rfid, args=(1,))
rfid_thread.start()
print("rfid start")

main_thread = threading.Thread(target=main, args=(1,))
main_thread.start()
print("rfid start")

# bikin thread untuk main program

if __name__ == "__main__":
    app.run()


























# def main():

#     humidity, temperature = get_sensor_suhu_data()

#     kirim_suhu("suhu", temperature)
#     kirim_suhu("kelembaban", humidity)
    # baca_rfid()

    # state = lampu()
    # state = ac()
    # state = tv()


# kirim_suhu()

# def main():
#     print("Program dimulai")
#     menerima_data_lampu()
#     print("Program selesai")

# if __name__ == "__main__":
#     main()

# menerima_data_ac()
# ac()

# menerima_data_tv()
# tv()

# while True:
#     time.sleep(1)
#     tv_toogle = menerima_data_tv() #menerima data dari ubi
#     tv(tv_toogle) #menyalakan atau mematikan tv
#     print('tv: ', tv_toogle)
#     ac_toogle = menerima_data_ac() #menerima data dari ubi
#     tv(tv_toogle) #menyalakan atau mematikan tv
#     print('ac: ', ac_toogle)
#     lampu_toogle = menerima_data_lampu() #menerima data dari ubi
#     tv(tv_toogle) #menyalakan atau mematikan tv
#     print('lampu: ', lampu_toogle)
#     temperature = random.uniform(25, 30)
#     kelembapan = random.uniform(10, 20)
#     kirim_suhu(temperature=temperature, humidity=kelembapan)
#     print('----') # hanya pembatas


'''
baca sensor suhu
kirim sensor suhu

ambil data lampu, ac, dan tv
matikan/nayalakn lampu, ac, dan tv

RFID diwaktu tambahan, karena ada tamopilan absensinya
'''



# tulis_rfid(name="NAUFI")
# id, text=baca_rfid()
# print(text)
# time.sleep(1)
# GPIO.cleanup()