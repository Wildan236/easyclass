import requests

# module connect ke ubidots
# bisa mengirim data sensor suhu dan kelembapan
# bisa menerima toogle ac, tv, dan lampu

'''
bari ini dicopy dari lampu-ubi.py
# Ubidots API URL dan Token
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/"
TOKEN = "BBFF-2jXFcArgZADJPrXdNDezHs4Q95gudr"
DEVICE_LABEL = "easyclass"
VARIABLE_LABEL1 = "ac"
VARIABLE_LABEL2 = "tv"
'''

# Ubidots API URL dan Token
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/easyclass/{variable_label}" #kurang {variable_label}
TOKEN = "BBFF-2jXFcArgZADJPrXdNDezHs4Q95gudr"
VARIABLE_LABEL1 = "ac"
VARIABLE_LABEL2 = "tv"
VARIABLE_LABEL3 = "kelembaban"
VARIABLE_LABEL4 = "suhu"
VARIABLE_LABEL5 = "lampu"


#kirim data suhu dan kelembapan
def kirim_suhu(humidity, temperature):
    url = "https://industrial.api.ubidots.com/api/v1.6/devices/easyclass"
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    payload = {
        "suhu": temperature,
        "kelembaban": humidity
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Data successfully sent to Ubidots")
        else:
            print("Failed to send data to Ubidots")
    except Exception as e:
        print("Error:", e)

#menerima data toogle lampu
def menerima_data_lampu(): #seharusnya sudah benar 
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(variable_label=VARIABLE_LABEL5)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None


#menerima data toogle ac
def menerima_data_ac(): #seharusnya sudah benar 
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(variable_label=VARIABLE_LABEL1)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None

    
#menerima data toogle tv
def menerima_data_tv(): #seharusnya sudah benar 
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(variable_label=VARIABLE_LABEL2)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None

#tambahkan cara penggunaannya
#contoh memanggil TV
# import time
# import random
# while True:
#     time.sleep(1)
#     tv_toogle = menerima_data_tv() #menerima data dari ubi
#     # tv(tv_toogle) #menyalakan atau mematikan tv
#     print('tv: ', tv_toogle)
#     ac_toogle = menerima_data_ac() #menerima data dari ubi
#     # tv(tv_toogle) #menyalakan atau mematikan tv
#     print('ac: ', ac_toogle)
#     lampu_toogle = menerima_data_lampu() #menerima data dari ubi
#     # tv(tv_toogle) #menyalakan atau mematikan tv
#     print('lampu: ', lampu_toogle)
#     temperature = random.uniform(25, 30)
#     kelembaban = random.uniform(10, 20)
#     kirim_suhu(temperature=temperature, humidity=kelembapan)
#     print('----') # hanya pembatas

