import requests
from datetime import datetime
import time
import smtplib

def is_night():
    # get sunset time
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise_time = data["results"]["sunrise"]
    sunset_time = data["results"]["sunset"]
    # get my time
    time_now = datetime.now().hour
    if time_now >= sunset_time and time_now <= sunrise_time:
        return True
    else:
        return False

def iss_is_overhead():
    # get iss current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    if abs(MY_LAT - latitude < 0.1) and abs(MY_LONG - longitude < 0.1):
        return True
    else:
        return False

MY_LAT = 37.253620
MY_LONG = 127.073429
my_position = (MY_LAT, MY_LONG)

parameter = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

my_email = "sendingtest0001@gmail.com"
password = "uadqtratvrlwtetu"

# main code
while(1): 
    if iss_is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= "sendingtest0002@gmail.com",
                msg= "Subject:Look up the sky:)\n\nLook up the sky!\nAnd try to find a ISS unit!")
    time.sleep(60)

# if iss come close to my current position & current time is after sunset,
# send mail to me, "Look up the sky" + run every 60 sec