#! /usr/bin/python3

# collect two different date from user
# use datetime module to calculate the intber of days between the the two days
# output result for user

import datetime,sys

year1 = int(sys.argv[1])
month1 = int(sys.argv[2])
day1 = int(sys.argv[3])
year2 = int(sys.argv[4])
month2 = int(sys.argv[5])
day2 = int(sys.argv[6])

def calculator():
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    diff = date2 - date1
    return diff.days

print(calculator())
