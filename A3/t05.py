year = int(input("Enter a year: "))
year100 = year % 100
year400 = year % 400
year4 = year % 4
if year100 == 0 and year400 == 0:
    leap = "Y"
elif year100 > 0 and year4 == 0:
    leap = "Y"
else:
    leap = "N"
#print
if leap == "Y":
    print(f"In the February of {year}, the number of days are 29.")
else:
    print(f"In the February of {year}, the number of days are 28.")