import requests
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "ce89ee1a2f6f67562fd5b371f1957b8e"

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
    print("Bring an umbrella")

