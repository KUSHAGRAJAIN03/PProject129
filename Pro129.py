import pandas as pd
import csv
data= []
data2 = []
with open ("project127.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
with open ("project128.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)
radius_list = list(data)
radius_list
h1 = data[0]
h1
h2 =data2[0]
h2
headers = h1+h2


remaining_data = data[1:]
remaining_data2 = data2[1:]

data_final = []
for index,data_row in enumerate(remaining_data):
    data_final.append(remaining_data[index]+remaining_data2[index])

with open ("Project129.csv","a+",encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data_final)
    