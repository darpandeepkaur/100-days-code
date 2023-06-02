import os
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACd2959dd4334810bb445825d75657866b"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 49.2827,
    "lon": 123.1207,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+19894478981",
        to="+17788837499"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's all clear, Have fun ;)",
        from_="+19894478981",
        to="+17788837499"
    )
    print(message.status)
    