# ----------------------------------------------------------------------------------------------------
# 15.Create a Student class using a constructor that accepts name, age, and course. Display all details.
# -----------------------------------------------------------------------------------------------------
# class Student:

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Course:", self.course)


# student1 = Student("Bhumika", 21, "DA")

# student1.display()

# OUTPUT:
# Name: Bhumika
# Age: 21
# Course: DA


# --------------------------------------------------------------------------------------------------
# 16.Create an Employee class using a constructor that accepts employee name, salary, and department.
# ---------------------------------------------------------------------------------------------------
# class Employee:

#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)


# employee1 = Employee("Rahul", 35000, "IT")

# employee1.display()


# OUTPUT:
# Name: Rahul
# Salary: 35000
# Department: IT


# -----------------------------------------------------------------------------------------------------------
# 17.Create a Car class using a constructor that accepts company, model, and price.
# ------------------------------------------------------------------------------------------------------------
# class Car:

#     def __init__(self, company, model, price):
#         self.company = company
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Company:", self.company)
#         print("Model:", self.model)
#         print("Price:", self.price)


# car1 = Car("Toyota", "Fortuner", 3500000)

# car1.display()

# OUTPUT:
# Company: Toyota
# Model: Fortuner
# Price: 3500000


# ------------------------------------------------------------------------------------------------------------------------
# 18.Create a Mobile class using a constructor that accepts brand, model, and price.
# ------------------------------------------------------------------------------------------------------------------------
# class Mobile:

#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)


# mobile1 = Mobile("Samsung", "Galaxy S24", 70000)

# mobile1.display()


# OUTPUT:
# Brand: Samsung
# Model: Galaxy S24
# Price: 70000


# -------------------------------------------------------------------------------------------------
# 19.Create a Book class using a constructor that accepts title, author, and price.
# ---------------------------------------------------------------------------------------------------
# class Book:

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)


# book1 = Book("Python Basics", "John Smith", 500)

# book1.display()

# OUTPUT:
# Title: Python Basics
# Author: John Smith
# Price: 500



# -----------------------------------------------------------------------------------------------------------------------
# 20.Create a Product class using a constructor that accepts product name, price, and quantity. Calculate the total price.
# ------------------------------------------------------------------------------------------------------------------------
# class Product:

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity


# product1 = Product("Laptop", 50000, 2)

# print("Product:", product1.name)
# print("Price:", product1.price)
# print("Quantity:", product1.quantity)
# print("Total Price:", product1.total_price())


# OUTPUT:
# Product: Laptop
# Price: 50000
# Quantity: 2
# Total Price: 100000



# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# 21.Create a BankAccount class using a constructor that accepts account holder name and balance. Create methods for deposit, withdrawal, and balance display.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def display_balance(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)


# account = BankAccount("Bhumika", 10000)

# account.deposit(5000)
# account.withdraw(2000)
# account.display_balance()

# OUTPUT:
# Deposited: 5000
# Withdrawn: 2000
# Account Holder: Bhumika
# Balance: 13000


# ----------------------------------------------------------------------------------------------------------
# 22.Create a Rectangle class using a constructor that accepts length and width. Calculate area and perimeter.
# ------------------------------------------------------------------------------------------------------------
# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# rectangle1 = Rectangle(10, 5)

# print("Area:", rectangle1.area())
# print("Perimeter:", rectangle1.perimeter())

# OUTPUT:
# Area: 50
# Perimeter: 30



# -----------------------------------------------------------------------------------------------------------
# 23.Create a Circle class using a constructor that accepts radius. Calculate area and circumference.
# --------------------------------------------------------------------------------------------------------------
# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius


# circle1 = Circle(7)

# print("Area:", circle1.area())
# print("Circumference:", circle1.circumference())


# OUTPUT:
# Area: 153.86
# Circumference: 43.96


# ----------------------------------------------------------------------------------------------------------------------------
# 24.Create a Student class using a constructor that accepts name and three subject marks. Calculate total and percentage.
# ----------------------------------------------------------------------------------------------------------------------------

# class Student:

#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def calculate(self):
#         total = self.m1 + self.m2 + self.m3
#         percentage = total / 3

#         print("Name:", self.name)
#         print("Total:", total)
#         print("Percentage:", percentage)


# student1 = Student("Bhumika", 80, 85, 90)

# student1.calculate()


# OUTPUT:
# Name: Bhumika
# Total: 255
# Percentage: 85.0


# ------------------------------------------------------------------------------------------------------------------------------------------
# 25.Create an Employee class using a constructor that accepts name and monthly salary. Calculate annual salary.
# ------------------------------------------------------------------------------------------------------------------------------------------
# class Employee:

#     def __init__(self, name, monthly_salary):
#         self.name = name
#         self.monthly_salary = monthly_salary

#     def annual_salary(self):
#         return self.monthly_salary * 12


# employee1 = Employee("Rahul", 30000)

# print("Employee:", employee1.name)
# print("Monthly Salary:", employee1.monthly_salary)
# print("Annual Salary:", employee1.annual_salary())

# OUTPUT:
# Employee: Rahul
# Monthly Salary: 30000
# Annual Salary: 360000



# ---------------------------------------------------------------------------------------------------------------------------
# 26.Create a ShoppingCart class using a constructor that accepts product name, price, and quantity. Calculate the total bill.
# -----------------------------------------------------------------------------------------------------------------------------
# class ShoppingCart:

#     def __init__(self, product_name, price, quantity):
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

#     def total_bill(self):
#         return self.price * self.quantity


# cart = ShoppingCart("Shoes", 2000, 3)

# print("Product:", cart.product_name)
# print("Price:", cart.price)
# print("Quantity:", cart.quantity)
# print("Total Bill:", cart.total_bill())

# OUTPUT:
# Product: Shoes
# Price: 2000
# Quantity: 3
# Total Bill: 6000



# ------------------------------------------------------------------------------------------------------------
# 27.Create a Laptop class using a constructor that accepts brand, RAM, storage, and price. Display all details.
# -------------------------------------------------------------------------------------------------------------------
# class Laptop:

#     def __init__(self, brand, ram, storage, price):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)
#         print("Storage:", self.storage)
#         print("Price:", self.price)


# laptop1 = Laptop("Dell", "16GB", "512GB SSD", 65000)

# laptop1.display()

# OUTPUT:
# Brand: Dell
# RAM: 16GB
# Storage: 512GB SSD
# Price: 65000


# --------------------------------------------------------------------------------------------------------------------------------
# 28.Create a Customer class using a constructor that accepts customer ID, name, mobile number, and city. Display customer details
# -----------------------------------------------------------------------------------------------------------------------------------
# class Customer:

#     def __init__(self, customer_id, name, mobile, city):
#         self.customer_id = customer_id
#         self.name = name
#         self.mobile = mobile
#         self.city = city

#     def display(self):
#         print("Customer ID:", self.customer_id)
#         print("Name:", self.name)
#         print("Mobile:", self.mobile)
#         print("City:", self.city)


# customer1 = Customer(101, "Bhumika", "9876543210", "Solapur")

# customer1.display()


# OUTPUT:
# Customer ID: 101
# Name: Bhumika
# Mobile: 9876543210
# City: Solapur



# ---------------------------------------------------------------------------------------------------------------------------------
# 29.Create a Salary class using a constructor that accepts employee name and basic salary. Calculate:
# ------------------------------------------------------------------------------------------------------------------------------------
# class Salary:

#     def __init__(self, employee_name, basic_salary):
#         self.employee_name = employee_name
#         self.basic_salary = basic_salary

#     def calculate(self):
#         hra = self.basic_salary * 0.20
#         da = self.basic_salary * 0.10
#         gross_salary = self.basic_salary + hra + da

#         print("Employee Name:", self.employee_name)
#         print("Basic Salary:", self.basic_salary)
#         print("HRA:", hra)
#         print("DA:", da)
#         print("Gross Salary:", gross_salary)


# salary1 = Salary("Bhumika", 30000)

# salary1.calculate()


# OUTPUT:
# Employee Name: Bhumika
# Basic Salary: 30000
# HRA: 6000.0
# DA: 3000.0
# Gross Salary: 39000.0



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 30.Create a Result class using a constructor that accepts student name and marks of five subjects. Calculate total, percentage, and pass/fail result
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# class Result:

#     def __init__(self, name, m1, m2, m3, m4, m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5

#     def calculate(self):
#         total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#         percentage = total / 5

#         if percentage >= 40:
#             result = "Pass"
#         else:
#             result = "Fail"

#         print("Student Name:", self.name)
#         print("Total:", total)
#         print("Percentage:", percentage)
#         print("Result:", result)


# student1 = Result("Bhumika", 80, 75, 85, 90, 70)

# student1.calculate()

# OUTPUT:
# Student Name: Bhumika
# Total: 400
# Percentage: 80.0
# Result: Pass



# -------------------------------------------------------------------------------------------------------------------------------------------------
# 31.Create a Product class using a constructor that accepts product name, price, and discount percentage. Calculate the final price after discount.
# --------------------------------------------------------------------------------------------------------------------------------------------------
# class Product:

#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self.discount = discount

#     def final_price(self):
#         discount_amount = self.price * self.discount / 100
#         return self.price - discount_amount


# product1 = Product("Mobile", 20000, 10)

# print("Product:", product1.name)
# print("Original Price:", product1.price)
# print("Discount:", product1.discount, "%")
# print("Final Price:", product1.final_price())


# OUTPUT:
# Product: Mobile
# Original Price: 20000
# Discount: 10 %
# Final Price: 18000.0



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 32.Create an ElectricityBill class using a constructor that accepts customer name and units consumed. Calculate the electricity bill based on units.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class ElectricityBill:

#     def __init__(self, customer_name, units):
#         self.customer_name = customer_name
#         self.units = units

#     def calculate_bill(self):

#         if self.units <= 100:
#             bill = self.units * 5

#         elif self.units <= 200:
#             bill = (100 * 5) + ((self.units - 100) * 7)

#         else:
#             bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

#         print("Customer Name:", self.customer_name)
#         print("Units Consumed:", self.units)
#         print("Electricity Bill: ₹", bill)


# customer1 = ElectricityBill("Bhumika", 250)

# customer1.calculate_bill()


# OUTPUT:
# Customer Name: Bhumika
# Units Consumed: 250
# Electricity Bill: ₹ 1700


# --------------------------------------------------------------------------------------------------------------------------------------------
# 33.Create a Travel class using a constructor that accepts passenger name, source, destination, and ticket price. Display the ticket details
# ---------------------------------------------------------------------------------------------------------------------------------------------
# class Travel:

#     def __init__(self, passenger_name, source, destination, ticket_price):
#         self.passenger_name = passenger_name
#         self.source = source
#         self.destination = destination
#         self.ticket_price = ticket_price

#     def display(self):
#         print("Passenger Name:", self.passenger_name)
#         print("Source:", self.source)
#         print("Destination:", self.destination)
#         print("Ticket Price:", self.ticket_price)


# travel1 = Travel("Bhumika", "Solapur", "Pune", 500)

# travel1.display()


# OUTPUT:
# Passenger Name: Bhumika
# Source: Solapur
# Destination: Pune
# Ticket Price: 500



# -------------------------------------------------------------------------------------------------------------------------------
# 34.Create a BankAccount class and create with different account holder names and balances. Display the details of all three accounts.
# -------------------------------------------------------------------------------------------------------------------------------------------
# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def display(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)
#         print("--------------------")


# account1 = BankAccount("Bhumika", 10000)
# account2 = BankAccount("Rahul", 15000)
# account3 = BankAccount("Priya", 20000)

# account1.display()
# account2.display()
# account3.display()


# OUTPUT:
# Account Holder: Bhumika
# Balance: 10000
# --------------------
# Account Holder: Rahul
# Balance: 15000
# --------------------
# Account Holder: Priya
# Balance: 20000
# --------------------


# -------------------------------------------------------------------------------------------------------
# 35.Create a Rectangle class with methods to calculate area and perimeter.
# -----------------------------------------------------------------------------------------------------------
# class Rectangle:

#     def area(self, length, width):
#         return length * width

#     def perimeter(self, length, width):
#         return 2 * (length + width)


# rectangle1 = Rectangle()

# print("Area:", rectangle1.area(10, 5))
# print("Perimeter:", rectangle1.perimeter(10, 5))



# OUTPUT:
# Area: 50
# Perimeter: 30


