# Take 5 employee names
file = open("employees.txt", "w")

for i in range(5):
    name = input("Enter employee name: ")
    file.write(name + "\n")

file.close()

print("Employee names saved successfully")

# Enter employee name: bhumika
# Enter employee name: nakshtra
# Enter employee name: vidya
# Enter employee name: sneha
# Enter employee name: aarya
# Employee names saved successfully