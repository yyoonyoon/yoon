import pandas

data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_num = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_num = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_num = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_num, cinnamon_num, black_num]
}

df = pandas.DataFrame(data_dict)
df.to_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#25/Squirrel_Color_Count")