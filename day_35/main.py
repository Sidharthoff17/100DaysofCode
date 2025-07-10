import requests
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "ce89ee1a2f6f67562fd5b371f1957b8e"

weather_params = {
    "lat": -37.813629,
    "lon": 144.963058,
    "appid": API_KEY
}

response = requests.get(OWN_ENDPOINT, params= weather_params)
print(response.json())
