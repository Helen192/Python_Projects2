import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('http://api.open-notify.org/iss-now.json') 
    data = r.json()  # convert data in website to json format
    text = f"Latitude: {data['iss_position']['latitude']} \nLongitude: {data['iss_position']['longitude']} \nTimestamp: {data['timestamp']}"

    while True:
        t = ToastNotifier()
        t.show_toast("Position of ISS", text, duration=20)
        time.sleep(60)
update()


