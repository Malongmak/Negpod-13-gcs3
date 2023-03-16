#!/usr/bin/python3
month = input("Enter any month: >  ")
longmonths = ["january", "march","may", "july", "august","october","december"]
shortmonths = [ "aprl", "june", "september", "november"]
february = ["february"]
search = month.lower()
lon = longmonths.count(search)
sho = shortmonths.count(search)
feb = february.count(search)

if lon == 1 :
    print("The month of " + month +  " has 31 days")
elif sho == 1 :
    print("The month of " + month +  " has 30  days")
elif feb == 1 : 
    print("The month of " + month +  " has 28 0r 29  days")
else :
    print("please enter a proper month")
