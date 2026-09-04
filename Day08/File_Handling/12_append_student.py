# Append a new student
# file = open("students.txt", "a")

# file.write("Rohit\n")

# file.close()

# print("New student added successfully")


# 14.Append numbers 11 to 20
file = open("numbers.txt", "a")

for i in range(11, 21):
    file.write(str(i) + "\n")

file.close()

print("Numbers 11 to 20 added successfully")


