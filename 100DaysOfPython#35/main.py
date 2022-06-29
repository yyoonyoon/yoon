import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from data import *
import os

account_sid = "AC55827d18fea72f6eae91a59b0e172e70"
auth_token = "c9b885e38020b9e0ba574a793b47b01b"

URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_API = "7e526dde995950fa98c7cae2ad71a2a9"
MUM_API = "e20526684005d39be7e8e8938e6a4cdd"
DAD_API = "bd6842ecce4293cdca39bf921592fe28"
JAMMIN_API = "cf2a75712af341103db17f027091e516"
EUNKONG_API = "5e25d84d4bd5e548f8ac6c34a0bdb83e"

my_weather_params = {
    "lat" : 37.253611, 
    "lon" : 127.073371,
    "appid" : MY_API,
    "exclude" : "minutely"
}

my_response =requests.get(url= URL, params= my_weather_params)
print(my_response.status_code) # return Error code
my_weather_data = my_response.json() # change reponse data to json.

id_data = []
rainy_times = []

def check_rain():
    for i in range(0,18):
        id_data.append(my_weather_data["current"]["weather"][0]["id"])
        id_data.append(my_weather_data["hourly"][i]["weather"][0]["id"])
        if id_data[i] < 700:
            proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
            print(f"It will rain after {i}hours later. Get your umbrella☂️.")
            rainy_times.append(i+7)
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                        body=f"\n오늘 {rainy_times} 시에 비가 올 예정이니, 우산을 꼭 챙기세요!!",
                        from_='++18303965432',
                        to='+821066075054'
                    )
    print(message.status)
check_rain()
print(id_data)