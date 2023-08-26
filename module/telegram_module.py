# send-message-to-telegram.py
# by www.ShellHacks.com

import requests

def send_to_telegram(message):

    apiToken = '6503965435:AAHLzojyzye2AFQ8lPNU9yuK3YFVKFQWuE4'
    chatID = '5270476923'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

#testing
#send_to_telegram("Sensor suhu mendeteksi Temperature dan Kelembaban yang tidak nomal, SEGERA PERIKSA APLIKASI!!!")