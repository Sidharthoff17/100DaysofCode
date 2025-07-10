#BY SIDHARTH RAO on 10/7
import requests
import os
from twilio.rest import Client
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = "AC83c2563ea55ad901675bd3cc58e56156"
auth_token= os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

weather_params = {
    "lat": -37.813629,
    "lon": 144.963058,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWN_ENDPOINT, params= weather_params)
response.raise_for_status()
weather_data = response.json()

#checker for rain
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain in Melbourne Victoria in the next 4 hours :(",
        from_="+16062120104",
        to="+61401795190",
    )
    print(message.status)
