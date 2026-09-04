# Store numbers 1 to 10
# file = open("numbers.txt", "w")

# for i in range(1, 11):
#     file.write(str(i) + "\n")

# file.close()

# print("Numbers 1 to 10 saved successfully")



# Take 5 numbers from user
file = open("numbers.txt", "w")

for i in range(5):
    number = input("Enter number: ")
    file.write(number + "\n")

file.close()

print("Numbers saved successfully")

# output:
# Enter number: 03
# Enter number: 20
# Enter number: 25
# Enter number: 22
# Enter number: 30
# Numbers saved successfully