# 29.Create a Student class and use self.name and self.marks to display student details.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# s = Student("Bhumika", 85)
# s.display()


# output:
# Name: Bhumika
# Marks: 85


# ----------------------------------------------------------------------------------------------------------
# 30.Create an Employee class and use self to access employee salary.
# -----------------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     def display_salary(self):
#         print("Salary:", self.salary)

# e = Employee(45000)
# e.display_salary()

# output:
# Salary: 45000

# -----------------------------------------------------------------------------------------------------------------------
# 31.Create a Car class and use self.brand and self.model inside a method.
# -----------------------------------------------------------------------------------------------------------------------
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)

# car = Car("Toyota", "Fortuner")
# car.display()


# OUTPUT:
# Brand: Toyota
# Model: Fortuner


# ---------------------------------------------------------------------------------------------------------------------
# 32.Create a Product class and use self.price inside a method to calculate total price.
# ----------------------------------------------------------------------------------------------------------------------------
# class Product:
#     def __init__(self, price, quantity):
#         self.price = price
#         self.quantity = quantity

#     def calculate_total(self):
#         total = self.price * self.quantity
#         print("Total Price:", total)

# product = Product(500, 3)
# product.calculate_total()

# OUTPUT:
# Total Price: 1500


# ------------------------------------------------------------------------------------------------------------------
# 33.Create a Student class with a method that prints "Hello" followed by the student's name using self.
# -------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Hello", self.name)

# student = Student("Bhumika")
# student.hello()

# OUTPUT:
# Hello Bhumika


# ---------------------------------------------------------------------------------------------------------------------------
# 34.Create a BankAccount class and use self.balance to display the current balance.
# ---------------------------------------------------------------------------------------------------------------------------
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def display(self):
#         print("Current Balance:", self.balance)

# account = BankAccount(30000)
# account.display()


# OUTPUT:
# Current Balance: 30000


# --------------------------------------------------------------------------------------------------------------------------------------
# 35.Create a Book class and use self.title and self.author in a method.
# -------------------------------------------------------------------------------------------------------------------------------------------
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)

# book = Book("The Alchemist", "Paulo Coelho")
# book.display()


# OUTPUT:
# Title: The Alchemist
# Author: Paulo Coelho


# -----------------------------------------------------------------------------------------------------------------------------------
# 36.Create a Mobile class and use self.price to display mobile price.
# -------------------------------------------------------------------------------------------------------------------------------------
# class Mobile:
#     def __init__(self, price):
#         self.price = price

#     def display_price(self):
#         print("Mobile Price:", self.price)

# mobile = Mobile(75000)
# mobile.display_price()

# OUTPUT:
# Mobile Price: 75000
