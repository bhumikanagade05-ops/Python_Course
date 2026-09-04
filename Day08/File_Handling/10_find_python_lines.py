# Display lines containing "Python"
file = open("messages.txt", "r")

for line in file:
    if "Python" in line:
        print(line.strip())

file.close()


# output:
# Hello Python
# Welcome to Python
# Python is easy