import csv
data1=[]
data2=[]

with open('dataset_1.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open('dataset_2_sorted.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data2.append(row)

header1=data1[0]
planet_data1=data1[1:]
header2=data2[0]
planet_data2=data2[1:]

headers=header1+header2
planetdata=[]
for index,data_row in enumerate(planet_data1):
    planetdata.append(planet_data1[index]+planet_data2[index])

with open('final2.csv','a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)