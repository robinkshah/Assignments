
weight = float(input("Enter weight of the package: "))
priority = input("Is it a priority package (Y/N): ")
priority_yes = "Y"
if priority==priority_yes:
    rate = 1.5
else:
    rate = 1
#weight2 = 2.0
#weight5 = 5.0
#weight11 = 11.0
if weight <= 2.0:
    rate = rate * 1.5
elif weight >= 2.0 and weight <= 5.0:
    rate = rate * 3.0
elif weight >= 5.0 and weight <= 11.0:
    rate = rate * 4.0
elif weight > 11.0:
    rate = rate * 4.75
else:
    exit()
cost = weight * rate
if priority==priority_yes:
    print(f"The cost of your priority package is: ${cost:.2f}")
else:
    print(f"The cost of your non-priority package is: ${cost:.2f}")

