# 1.Create a Student class with instance variables name, age, and marks. Create one object and display all details.

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

# student1 = Student("Bhumika", 21, 85)

# print("Name:", student1.name)
# print("Age:", student1.age)
# print("Marks:", student1.marks)

# output:
# Name: Bhumika
# Age: 21
# Marks: 85


# --------------------------------------------------------------------------------------------------------------------------------
# 2.Create an Employee class with name, salary, and department. Display employee details.
# ------------------------------------------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

# employee1 = Employee("Bhumii", 35000, "IT")

# print("Name:", employee1.name)
# print("Salary:", employee1.salary)
# print("Department:", employee1.department)

# output:
# Name: Bhumii
# Salary: 35000
# Department: IT




# -----------------------------------------------------------------------------------------------------------------------------------------
# 3.Create a Car class with brand, model, and price. Create two objects and display their details.
# ---------------------------------------------------------------------------------------------------------------------------------------------
# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

# car1 = Car("Toyota", "Fortuner", 4000000)
# car2 = Car("Hyundai", "Creta", 1800000)

# print(car1.brand, car1.model, car1.price)
# print(car2.brand, car2.model, car2.price)


# output:
# Toyota Fortuner 4000000
# Hyundai Creta 1800000


# --------------------------------------------------------------------------------------------------------------------------
# 4.Create a Book class with title, author, and price. Create an object and display the information.
# ---------------------------------------------------------------------------------------------------------------------------

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

# book1 = Book("Python Programming", "John Smith", 500)

# print("Title:", book1.title)
# print("Author:", book1.author)
# print("Price:", book1.price)

# output:
# Title: Python Programming
# Author: John Smith
# Price: 500


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# 5.Create a Mobile class with brand, model, and price. Display mobile details.
# -------------------------------------------------------------------------------------------------------------------------------------

# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

# mobile1 = Mobile("Samsung", "S25", 80000)

# print("Brand:", mobile1.brand)
# print("Model:", mobile1.model)
# print("Price:", mobile1.price)

# output:
# Brand: Samsung
# Model: S25
# Price: 80000


# ---------------------------------------------------------------------------------------------------------------------------
# 6.Create a Product class with product_name, price, and quantity. Display all values.
# ---------------------------------------------------------------------------------------------------------------------------

# class Product:
#     def __init__(self, product_name, price, quantity):
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

# product1 = Product("Laptop", 60000, 2)

# print("Product:", product1.product_name)
# print("Price:", product1.price)
# print("Quantity:", product1.quantity)


# output:
# Product: Laptop
# Price: 60000
# Quantity: 2


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7.Create a Person class with name, age, and city. Create three objects and display their information.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

# p1 = Person("Bhumii", 22, "Pune")
# p2 = Person("Naksh", 23, "Mumbai")
# p3 = Person("Niraj", 21, "Nashik")

# print(p1.name, p1.age, p1.city)
# print(p2.name, p2.age, p2.city)
# print(p3.name, p3.age, p3.city)


# output:
# Bhumii 22 Pune
# Naksh 23 Mumbai
# Niraj 21 Nashik


# ------------------------------------------------------------------------------------------------------------------------------
# 8.Create a Laptop class with brand, ram, storage, and price. Display laptop details.
# ------------------------------------------------------------------------------------------------------------------------------
# class Laptop:
#     def __init__(self, brand, ram, storage, price):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

# laptop1 = Laptop("Dell", "16GB", "512GB", 65000)

# print("Brand:", laptop1.brand)
# print("RAM:", laptop1.ram)
# print("Storage:", laptop1.storage)
# print("Price:", laptop1.price)


# output:
# Brand: Dell
# RAM: 16GB
# Storage: 512GB
# Price: 65000


# -----------------------------------------------------------------------------------------------------------------------
# 9.Create a Movie class with name, actor, actress, and rating. Display movie information.
# ------------------------------------------------------------------------------------------------------------------------
# class Movie:
#     def __init__(self, name, actor, actress, rating):
#         self.name = name
#         self.actor = actor
#         self.actress = actress
#         self.rating = rating

# movie1 = Movie("Example Movie", "Ranveer Singh", "Alia Bhatt", 8.5)

# print("Movie:", movie1.name)
# print("Actor:", movie1.actor)
# print("Actress:", movie1.actress)
# print("Rating:", movie1.rating)


# output:
# Movie: Example Movie
# Actor: Ranveer Singh
# Actress: Alia Bhatt
# Rating: 8.5


# -----------------------------------------------------------------------------------------------------------------
# 10.Create a BankAccount class with account_holder, account_number, and balance. Display account details.
# -------------------------------------------------------------------------------------------------------------------
# class BankAccount:
#     def __init__(self, account_holder, account_number, balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance

# account1 = BankAccount("Bhumika", "1234567890", 25000)

# print("Account Holder:", account1.account_holder)
# print("Account Number:", account1.account_number)
# print("Balance:", account1.balance)


# output:
# Account Holder: Bhumika
# Account Number: 1234567890
# Balance: 25000


# ---------------------------------------------------------------------------------------------------------------------------
# 11.Create a Teacher class with name, subject, and salary. Create two objects.
# ----------------------------------------------------------------------------------------------------------------------------
# class Teacher:
#     def __init__(self, name, subject, salary):
#         self.name = name
#         self.subject = subject
#         self.salary = salary

# t1 = Teacher("Chetan sir", "Python", 45000)
# t2 = Teacher("Mahesh sir", "Java", 50000)

# print(t1.name, t1.subject, t1.salary)
# print(t2.name, t2.subject, t2.salary)


# output:
# Chetan sir Python 45000
# Mahesh sir Java 50000


# -------------------------------------------------------------------------------------------------------------------------------------------
# 12.Create a CollegeStudent class with name, roll_no, course, and year.
# -------------------------------------------------------------------------------------------------------------------------------------------

# class CollegeStudent:
#     def __init__(self, name, roll_no, course, year):
#         self.name = name
#         self.roll_no = roll_no
#         self.course = course
#         self.year = year

# student = CollegeStudent("Bhumika", 101, "DA", 3)

# print(student.name)
# print(student.roll_no)
# print(student.course)
# print(student.year)


# OUTPUT:
# Bhumika
# 101
# DA
#  3

# ------------------------------------------------------------------------------------------------------------------------
# 13.Create a HospitalPatient class with name, age, disease, and room_no.
# -------------------------------------------------------------------------------------------------------------------------
# class HospitalPatient:
#     def __init__(self, name, age, disease, room_no):
#         self.name = name
#         self.age = age
#         self.disease = disease
#         self.room_no = room_no

# patient = HospitalPatient("Amit", 35, "Fever", 205)

# print(patient.name)
# print(patient.age)
# print(patient.disease)
# print(patient.room_no)


# OUTPUT:
# Amit
# 35
# Fever
# 205


# ---------------------------------------------------------------------------------------------------------------------------------
# 14.Create a Laptop class and create five different laptop objects with different values.
# ---------------------------------------------------------------------------------------------------------------------------------
# class Laptop:
#     def __init__(self, brand, ram, storage, price):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

# l1 = Laptop("Dell", "8GB", "512GB", 50000)
# l2 = Laptop("HP", "16GB", "512GB", 65000)
# l3 = Laptop("Lenovo", "8GB", "256GB", 45000)
# l4 = Laptop("Asus", "16GB", "1TB", 75000)
# l5 = Laptop("Acer", "8GB", "512GB", 55000)

# print(l1.brand, l1.ram, l1.storage, l1.price)
# print(l2.brand, l2.ram, l2.storage, l2.price)
# print(l3.brand, l3.ram, l3.storage, l3.price)
# print(l4.brand, l4.ram, l4.storage, l4.price)
# print(l5.brand, l5.ram, l5.storage, l5.price)


# OUTPUT:
# Dell 8GB 512GB 50000
# HP 16GB 512GB 65000
# Lenovo 8GB 256GB 45000
# Asus 16GB 1TB 75000
# Acer 8GB 512GB 55000


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# 15.Create a Bike class with brand, model, color, and price.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# class Bike:
#     def __init__(self, brand, model, color, price):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price

# bike = Bike("Royal Enfield", "Classic 350", "Black", 220000)

# print(bike.brand)
# print(bike.model)
# print(bike.color)
# print(bike.price)

# OUTPUT:
# Royal Enfield
# Classic 350
# Black
# 220000


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 16.Create a Company class with company_name, location, and employees.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Company:
#     def __init__(self, company_name, location, employees):
#         self.company_name = company_name
#         self.location = location
#         self.employees = employees

# company = Company("Infosys", "Pune", 5000)

# print(company.company_name)
# print(company.location)
# print(company.employees)

# OUTPUT:
# Infosys
# Pune
# 5000



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 17.Create a Course class with course_name, duration, and fees.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Course:
#     def __init__(self, course_name, duration, fees):
#         self.course_name = course_name
#         self.duration = duration
#         self.fees = fees

# course = Course("Python Programming", "6 Months", 15000)

# print(course.course_name)
# print(course.duration)
# print(course.fees)


# OUTPUT:
# Python Programming
# 6 Months
# 15000


# ------------------------------------------------------------------------------------------------------------------------------------------------
# 18.Create a Restaurant class with name, location, and rating.
# -------------------------------------------------------------------------------------------------------------------------------------------------
# class Restaurant:
#     def __init__(self, name, location, rating):
#         self.name = name
#         self.location = location
#         self.rating = rating

# restaurant = Restaurant("Food Hub", "Pune", 4.5)

# print(restaurant.name)
# print(restaurant.location)
# print(restaurant.rating)


# OUTPUT:
# Food Hub
# Pune
# 4.5


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 19.Create a Flight class with flight_no, source, destination, and price.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Flight:
#     def __init__(self, flight_no, source, destination, price):
#         self.flight_no = flight_no
#         self.source = source
#         self.destination = destination
#         self.price = price

# flight = Flight("AI101", "Pune", "Delhi", 6500)

# print(flight.flight_no)
# print(flight.source)
# print(flight.destination)
# print(flight.price)


# OUTPUT:
# AI101
# Pune
# Delhi
# # 6500

# -----------------------------------------------------------------------------------------------------------------------------
# 20.Create a Hotel class with name, location, room_type, and price.
# ----------------------------------------------------------------------------------------------------------------------------
# class Hotel:
#     def __init__(self, name, location, room_type, price):
#         self.name = name
#         self.location = location
#         self.room_type = room_type
#         self.price = price

# hotel = Hotel("Taj Hotel", "Mumbai", "Deluxe", 8000)

# print(hotel.name)
# print(hotel.location)
# print(hotel.room_type)
# print(hotel.price)

# OUTPUT:
# Taj Hotel
# Mumbai
# Deluxe
# 8000








