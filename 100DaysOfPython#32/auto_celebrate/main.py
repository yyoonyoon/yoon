import pandas
import datetime as dt
import random
import smtplib

my_email = "sendingtest0001@gmail.com"
password = "uadqtratvrlwtetu"

time_of_now = dt.datetime.now()
today_tuple  = (time_of_now.month, time_of_now.day)

bday_data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#32/auto_celebrate/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bday_data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#32/\
auto_celebrate/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as text_file:
        contents = text_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs= birthday_person["email"], msg= f"Subject:Happy birthday:)\n\n{contents}")

# print(bday_data.loc[[0],:]) #0  Mum  dddd4@naver.com  19xx 12  xx
# print(bday_data.loc[[0],:]['month']) # 12
# folder_loc = "/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#32/auto_celebrate/letter_templates" # /letter_1.txt or /leter_2.txt ...


