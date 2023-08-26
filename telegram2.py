import requests
TOKEN = "6503965435:AAHLzojyzye2AFQ8lPNU9yuK3YFVKFQWuE4"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())