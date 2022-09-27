row = input("Enter the length of the row, in feet: ")
space = input("Enter the amount of space, in feet, used by an end-post assembly: ")
dist = input("Enter the distance, in feet, between each vine: ")
total_space = int(row) - int(space)*2
vines = total_space / int(dist)
vines = float(vines)
print(f"You have enough space for {vines} vines.")
