# with open("day25/weather_data.csv", mode="r") as weather:
#     data = weather.readlines()
#     print(data)

# import csv

# with open("day25/weather_data.csv", mode="r") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas

data = pandas.read_csv("day25/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# Tính trung bình nhiệt độ
# avg = round(sum(temp_list) / len(temp_list), 2)
# print(avg)
# print(data["temp"].mean())

# In ra nhiệt độ lớn nhất
# print(data["temp"].max())

# Lấy ra 1 cột
# print(data["condition"])
# print(data.condition)
# Lấy dữ liệu ra từ 1 dòng
# print(data[data.day == "Monday"])

# In ra dòng có nhiệt độ cao nhất trong tuần
# print(data[data.temp.max() == data.temp])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# temp_f = monday.temp[0] * 9 / 5 + 32
# print(temp_f)
#  Tạo DataFrames từ scratch
data_dict = {"student": ["Amny", "James", "Angela"], "score": [76, 56, 65]}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("day25/new_data.csv")
