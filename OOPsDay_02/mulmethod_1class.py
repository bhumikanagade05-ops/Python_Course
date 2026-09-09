# 37.Create a Calculator class containing add(), subtract(), multiply(), and divide() methods.

# class Calculator:

#     def add(self, a, b):
#         print("Addition:", a + b)

#     def subtract(self, a, b):
#         print("Subtraction:", a - b)

#     def multiply(self, a, b):
#         print("Multiplication:", a * b)

#     def divide(self, a, b):
#         print("Division:", a / b)


# c = Calculator()

# c.add(10, 5)
# c.subtract(10, 5)
# c.multiply(10, 5)
# c.divide(10, 5)



# output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0



# --------------------------------------------------------------------------------------------------------------------------------
# 38.Create a Student class containing display(), calculate_total(), and calculate_percentage() methods.
# ---------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def display(self):
#         print("Name:", self.name)

#     def calculate_total(self):
#         return self.marks1 + self.marks2 + self.marks3

#     def calculate_percentage(self):
#         total = self.calculate_total()
#         return total / 3


# s = Student("Bhumika", 85, 90, 80)

# s.display()
# print("Total:", s.calculate_total())
# print("Percentage:", s.calculate_percentage())




# output:
# Name: Bhumika
# Total: 255
# Percentage: 85.0


# -----------------------------------------------------------------------------------------------------------------------------------------------
# 39.Create an Employee class containing display(), calculate_annual_salary(), and calculate_bonus() methods.
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Name:", self.name)
#         print("Monthly Salary:", self.salary)

#     def calculate_annual_salary(self):
#         return self.salary * 12

#     def calculate_bonus(self):
#         return self.salary * 0.10


# e = Employee("Bhumii", 40000)

# e.display()
# print("Annual Salary:", e.calculate_annual_salary())
# print("Bonus:", e.calculate_bonus())


# output:
# Name: Bhumii
# Monthly Salary: 40000
# Annual Salary: 480000
# Bonus: 4000.0


# -----------------------------------------------------------------------------------------------------------------------
# # 40.Create a BankAccount class containing deposit(), withdraw(), and display_balance() methods.
# -----------------------------------------------------------------------------------------------------------------------
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         print("Balance:", self.balance)


# account = BankAccount(10000)

# account.display_balance()
# account.deposit(5000)
# account.display_balance()
# account.withdraw(3000)
# account.display_balance()


# output:
# Balance: 10000
# Deposited: 5000
# Balance: 15000
# Withdrawn: 3000
# Balance: 12000


# ---------------------------------------------------------------------------------------------------------------------------------
# 41.Create a Rectangle class containing area(), perimeter(), and display() methods.
# ----------------------------------------------------------------------------------------------------------------------------------
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

#     def display(self):
#         print("Length:", self.length)
#         print("Breadth:", self.breadth)
#         print("Area:", self.area())
#         print("Perimeter:", self.perimeter())


# r = Rectangle(10, 5)
# r.display()


# output:
# Length: 10
# Breadth: 5
# Area: 50
# Perimeter: 30


# ---------------------------------------------------------------------------------------------------------------------------------
# 42.Create a Circle class containing area(), circumference(), and display() methods.
# ---------------------------------------------------------------------------------------------------------------------------------
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

#     def display(self):
#         print("Radius:", self.radius)
#         print("Area:", self.area())
#         print("Circumference:", self.circumference())


# c = Circle(7)
# c.display()


# output:
# Radius: 7
# Area: 153.86
# Circumference: 43.96


# ------------------------------------------------------------------------------------------------------------------------------------
# 43.Create a Product class containing display(), calculate_total(), and apply_discount() methods.
# ---------------------------------------------------------------------------------------------------------------------------------------
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def display(self):
#         print("Product:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)

#     def calculate_total(self):
#         return self.price * self.quantity

#     def apply_discount(self, discount):
#         total = self.calculate_total()
#         discount_amount = total * discount / 100
#         final_price = total - discount_amount
#         return final_price


# p = Product("Laptop", 60000, 2)

# p.display()
# print("Total:", p.calculate_total())
# print("After 10% Discount:", p.apply_discount(10))


# output:
# Product: Laptop
# Price: 60000
# Quantity: 2
# Total: 120000
# After 10% Discount: 108000.0