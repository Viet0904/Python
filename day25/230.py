import pandas

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fun Color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_count, red_count, black_count],
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("day25/squirrel_count.csv")

# count_primary_fur_color = data["Primary Fur Color"].value_counts()
# print(type(count_primary_fur_color))
# data_list = count_primary_fur_color.to_csv("day25/squirrel_count.csv")
# data_dict = count_primary_fur_color
