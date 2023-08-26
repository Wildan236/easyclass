import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Ganti dengan pin GPIO tempat Anda menghubungkan sensor DHT22

def get_sensor_suhu_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f}%")
    return humidity, temperature

# while True:
#     get_sensor_suhu_data()
#     time.sleep(1)