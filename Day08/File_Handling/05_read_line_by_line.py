# 5️. Read file line by line

file = open("messages.txt", "r")

for line in file:
    print(line.strip())

file.close()


# output:
# Hello Python
# Welcome to Python
# Python is easy
# Practice every day
# Keep learning