from calendar import week
from multiprocessing import connection
import smtplib
import random
import datetime as dt
# from email.mime.text import MIMEText

with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#32/quotes.txt") as data_file:
    quotes_list = data_file.readlines()
    todays_quote = random.choice(quotes_list)

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
now = dt.datetime.now()
num_of_day = now.weekday() # obtain todays day num
name_of_weekday = weekdays[num_of_day]

my_email = "sendingtest0001@gmail.com"
password = "uadqtratvrlwtetu"
# msg = MIMEText(todays_quote)
# msg["Subject"] = "Today's quote!"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs="sendingtest0002@gmail.com", msg=f"Subject:Today's Motivation\n\nToday is {name_of_weekday}.\n This is today's quote. \
I hope you have a nice day!!\n\n{todays_quote}")
