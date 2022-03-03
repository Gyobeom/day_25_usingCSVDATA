# with open("weather_data.csv", "r") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     firtst = 0
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# high_temp = data["temp"].max()
# print(data[data.temp == high_temp])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)


data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" :[76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)












