import telebot
import subprocess
import json
import time

# Сенің мәліметтерің
TOKEN = "8711913443:AAFizqWhgtm9w58i2UD5PnckYiXWkKA1s2M"
CHAT_ID = "7594678193"
bot = telebot.TeleBot(TOKEN)

print("Seeker 2.0 LIVE + SPEED іске қосылды...")

def get_live_data():
    try:
        # GPS-тен жылдамдық пен координатты алу
        raw_data = subprocess.check_output(['termux-location'], timeout=20).decode('utf-8')
        data = json.loads(raw_data)
        return {
            "lat": data['latitude'],
            "lon": data['longitude'],
            "speed": round(data.get('speed', 0) * 3.6, 1) # км/сағ
        }
    except Exception as e:
        print(f"GPS қатесі: {e}")
        return None

# Бастапқы нүктені жіберу (1 сағаттық LIVE режим)
start_data = get_live_data()
if start_data:
    live_msg = bot.send_location(
        CHAT_ID, 
        start_data['lat'], 
        start_data['lon'], 
        live_period=3600
    )
    bot.send_message(CHAT_ID, f"🏁 Бақылау басталды!\nЖылдамдық: {start_data['speed']} км/сағ")

    while True:
        time.sleep(10) # 10 секунд сайын жаңарту
        new_data = get_live_data()
        
        if new_data:
            try:
                # Картадағы маркерді жылжыту
                bot.edit_message_live_location(
                    chat_id=CHAT_ID,
                    message_id=live_msg.message_id,
                    latitude=new_data['lat'],
                    longitude=new_data['lon']
                )
                
                # Жылдамдық 5 км/сағ-тан асса, хабарлама жіберу (немесе жай ғана лог)
                if new_data['speed'] > 5:
                    print(f"Нысана қозғалуда: {new_data['speed']} км/сағ")
            except Exception as e:
                pass
else:
    print("Қате: Бастапқы координат алынбады. GPS қосулы ма?")
