import time
import Adafruit_DHT
import requests

# Konfigurasi sensor DHT22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Ganti dengan pin GPIO tempat Anda menghubungkan sensor DHT22

# Konfigurasi Ubidots
UBIDOTS_TOKEN = "BBFF-2jXFcArgZADJPrXdNDezHs4Q95gudr"
DEVICE_LABEL = "easyclass"  # Ganti dengan label device yang Anda buat di Ubidots

def get_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

def send_to_ubidots(humidity, temperature):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
    headers = {"X-Auth-Token": UBIDOTS_TOKEN, "Content-Type": "application/json"}

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

if __name__ == "__main__":
    try:
        while True:
            humidity, temperature = get_sensor_data()
            if humidity is not None and temperature is not None:
                print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f}%")
                send_to_ubidots(humidity, temperature)
            else:
                print("Failed to retrieve data from the sensor.")
            time.sleep(0.1)  # Ubah angka 10 ke interval yang diinginkan (dalam detik)
    except KeyboardInterrupt:
        print("Terminated by the user")
