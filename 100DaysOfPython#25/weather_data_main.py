# import csv

# with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/weather_data.csv")\
# as weather_data:
#     data = csv.reader(weather_data)
#     temperture = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperture.append(int(row[1]))
#     print(temperture)

import pandas

data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/weather_data.csv")
data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# find maximum value
# temp_average = sum(temp_list) / len(temp_list) 정석적인 파이썬 방식
temp_average = data["temp"].mean() # pandas method 사용
temp_maximum = data["temp"].argmax()

# weather_data.csv에서 온도가 가장 높은 데이터가 있는 행을 구하기
data[data.temp == temp_maximum]
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32