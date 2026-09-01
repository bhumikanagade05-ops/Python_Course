# 1. Create a student dictionary
# student = {
#     "name": "Bhumika",
#     "age": 21,
#     "course": "DA"
# }

# print(student)

# output:
# {'name': 'Bhumika', 'age': 21, 'course': 'DA'}


# 2. Access values using keys
# student = {
#     "name": "Bhumika",
#     "age": 21,
#     "course": "DA"
# }

# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Course:", student["course"])

# OUTPUT:
# Name: Bhumika
# Age: 21
# Course: DA


# 3. Add a new key
# student = {
#     "name": "Bhumika",
#     "age": 21
# }

# student["city"] = "Solapur"

# print(student)

# OUTPUT:
# {'name': 'Bhumika', 'age': 21, 'city': 'Solapur'}



# 4. Update an existing value
# student = {
#     "name": "Bhumika",
#     "age": 21
# }

# student["age"] = 22

# print(student)

# OUTPUT:
# {'name': 'Bhumika', 'age': 22}



# 5. Delete a key

# student = {
#     "name": "Bhumika",
#     "age": 21,
#     "course": "DA"
# }

# del student["age"]

# print(student)


# OUTPUT:
# {'name': 'Bhumika', 'course': 'DA'}



# 6. Use keys(), values() and items()
# student = {
#     "name": "Bhumika",
#     "age": 21,
#     "course": "DA"
# }

# print("Keys:", student.keys())
# print("Values:", student.values())
# print("Items:", student.items())


# OUTPUT:
# Keys: dict_keys(['name', 'age', 'course'])
# Values: dict_values(['Bhumika', 21, 'DA'])
# Items: dict_items([('name', 'Bhumika'), ('age', 21), ('course', 'DA')])



# 7. Check whether a key exists
# student = {
#     "name": "Bhumika",
#     "age": 21,
#     "course": "DA"
# }

# if "name" in student:
#     print("Key exists")
# else:
#     print("Key does not exist")

# OUTPUT:
#  Key exists


# 8. Create a dictionary containing student marks
# marks = {
#     "Bhumika": 85,
#     "Niraj": 72,
#     "Atharva": 90,
#     "Nakshtra": 78
# }

# print(marks)

# output:
# {'Bhumika': 85, 'Niraj': 72, 'Atharva': 90, 'Nakshtra': 78}



# 9. Create a list of dictionaries for five students
# students = [
#     {"name": "Bhumika", "marks": 85},
#     {"name": "Rahul", "marks": 72},
#     {"name": "Priya", "marks": 90},
#     {"name": "Sneha", "marks": 78},
#     {"name": "Amit", "marks": 65}
# ]

# print(students)

# output:
# [{'name': 'Bhumika', 'marks': 85}, {'name': 'Rahul', 'marks': 72}, {'name': 'Priya', 'marks': 90}, {'name': 'Sneha', 'marks': 78}, {'name': 'Amit', 'marks': 65}]


# 10. Display students whose marks are greater than 75
# students = [
#     {"name": "Bhumika", "marks": 85},
#     {"name": "Nakshtra", "marks": 72},
#     {"name": "aarya", "marks": 90},
#     {"name": "Sneha", "marks": 78},
#     {"name": "Amit", "marks": 65}
# ]

# print("Students with marks greater than 75:")

# for student in students:
#     if student["marks"] > 75:
#         print(student["name"], "-", student["marks"])


# output:
# Bhumika - 85
# aarya - 90
# Sneha - 78
