#! /usr/bin/python3

import csv


colConstruct = []

with open("Kufre_Samuel_data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)

        colConstruct.append(row[1])

    csv_file.close()

print(colConstruct)

colConstruct.pop(0)

print (colConstruct)

newCol = []

for item in colConstruct:
    item = float(item)
    newCol.append(item)
print(newCol)

count = 0

for num in newCol:
    count = count + num
print(count)

averagecount = count / len(newCol)

print(averagecount)


'''if type(row[1]) == "int" or type(row[1]) == "int":
           colConstruct.append(row)
        else:
            break
        print(colConstruct)
'''
