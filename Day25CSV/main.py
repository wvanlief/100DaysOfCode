# with open("weather_data.csv", "r") as file: data = file.readlines()

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     header = next(data)
#     if header is not None:
#         for row in data:
#             temperatures.append(int(row[1]))
#             print(row)
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])