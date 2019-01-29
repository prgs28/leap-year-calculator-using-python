
year=int(input("enter the year"))
if(year%100==0):
    if(year%400==0):
        print("In", year, "february had 29 days")
    else:
        print("Its not a leap year")
else:
    if(year%4==0):
        print("In", year, "february had 29 days")
    else:
        print("Its not a leap year")
