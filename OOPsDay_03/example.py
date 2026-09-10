# 1. Create a BankAccount class with a private __balance variable. Add methods to deposit, withdraw, and
# display the balance.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Amount deposited:", amount)
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print("Amount withdrawn:", amount)
#         else:
#             print("Invalid amount or insufficient balance")

#     def display_balance(self):
#         print("Balance:", self.__balance)


# account = BankAccount(5000)
# account.deposit(1000)
# account.withdraw(2000)
# account.display_balance()



# output:
# Amount deposited: 1000
# Amount withdrawn: 2000
# Balance: 4000


# =======================================================================================================================
# 2. Create a Student class with private __name and __marks variables. Use getter and setter methods to
# read and update them.
# ===========================================================================================================================
# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         self.__marks = marks


# student = Student("Bhumika", 85)

# print("Name:", student.get_name())
# print("Marks:", student.get_marks())

# student.set_name("Rahul")
# student.set_marks(90)

# print("Updated Name:", student.get_name())
# print("Updated Marks:", student.get_marks())


# output:
# Name: Bhumika
# Marks: 85
# Updated Name: Rahul
# Updated Marks: 90


# ======================================================================================================================================
# 3. Create an Employee class with private __salary. Allow salary changes only through a setter that rejects
# negative values.
# =====================================================================================================================================
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def set_salary(self, salary):
#         if salary >= 0:
#             self.__salary = salary
#         else:
#             print("Salary cannot be negative")

#     def get_salary(self):
#         return self.__salary


# employee = Employee(30000)

# print("Salary:", employee.get_salary())

# employee.set_salary(40000)
# print("Updated Salary:", employee.get_salary())

# employee.set_salary(-5000)


# output:
# Salary: 30000
# Updated Salary: 40000
# Salary cannot be negative

# =========================================================================================================================================
# 4. Create a Person class with private __age. Create methods to set age and check whether the person is
# eligible to vote.
# ==========================================================================================================================================
# class Person:
#     def __init__(self, age):
#         self.__age = age

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Invalid age")

#     def is_eligible_to_vote(self):
#         return self.__age >= 18


# person = Person(20)

# print("Age:", person._Person__age)
# print("Eligible to vote:", person.is_eligible_to_vote())

# person.set_age(16)
# print("Eligible to vote:", person.is_eligible_to_vote())


# output:
# Age: 20
# Eligible to vote: True
# Eligible to vote: False


# ===========================================================================================================================================
# 5. Create a Product class with private __price. Prevent the price from being set to zero or a negative
# number.
# ============================================================================================================================================
# class Product:
#     def __init__(self, price):
#         self.__price = 0
#         self.set_price(price)

#     def set_price(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             print("Price must be greater than zero")

#     def get_price(self):
#         return self.__price


# product = Product(500)
# print("Price:", product.get_price())

# product.set_price(-100)

# output:
# Price: 500
# Price must be greater than zero


# =============================================================================================================================
# 6. Create a Mobile class with private __brand, __model, and __price. Add methods to set and display all
# details.
# ==============================================================================================================================
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price

#     def set_details(self, brand, model, price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price

#     def display(self):
#         print("Brand:", self.__brand)
#         print("Model:", self.__model)
#         print("Price:", self.__price)


# mobile = Mobile("Samsung", "S25", 80000)
# mobile.display()

# mobile.set_details("Apple", "iPhone 17", 90000)
# mobile.display()


# output:
# Brand: Samsung
# Model: S25
# Price: 80000
# Brand: Apple
# Model: iPhone 17
# Price: 90000


# ======================================================================================================================================
# 7. Create a Car class with a private __speed. Provide accelerate() and brake() methods and prevent speed
# from becoming negative.
# ========================================================================================================================================
# class Car:
#     def __init__(self):
#         self.__speed = 0

#     def accelerate(self, value):
#         if value > 0:
#             self.__speed += value

#     def brake(self, value):
#         if value > 0:
#             self.__speed -= value

#             if self.__speed < 0:
#                 self.__speed = 0

#     def display_speed(self):
#         print("Speed:", self.__speed)


# car = Car()

# car.accelerate(50)
# car.display_speed()

# car.brake(20)
# car.display_speed()

# car.brake(50)
# car.display_speed()

# output:
# Speed: 50
# Speed: 30
# Speed: 0


# =============================================================================================================================================
# 8. Create a Rectangle class with private __length and __width. Use methods to calculate area and
# perimeter.
# =============================================================================================================================================

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     def area(self):
#         return self.__length * self.__width

#     def perimeter(self):
#         return 2 * (self.__length + self.__width)


# rectangle = Rectangle(10, 5)

# print("Area:", rectangle.area())
# print("Perimeter:", rectangle.perimeter())


# output:
# Area: 50
# Perimeter: 30


# ====================================================================================================================================
# 9. Create a Circle class with private __radius. Use a setter to reject a radius less than or equal to zero.
# =====================================================================================================================================
# class Circle:
#     def __init__(self, radius):
#         self.__radius = 0
#         self.set_radius(radius)

#     def set_radius(self, radius):
#         if radius > 0:
#             self.__radius = radius
#         else:
#             print("Radius must be greater than zero")

#     def area(self):
#         return 3.14 * self.__radius * self.__radius


# circle = Circle(5)

# print("Area:", circle.area())

# circle.set_radius(-2)

# output:
# Area: 78.5
# Radius must be greater than zero


# ===============================================================================================================
# 10. Create an Account class with private __account_number and __balance. Display account information
# through a public method.
# ================================================================================================================
# class Account:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def display(self):
#         print("Account Number:", self.__account_number)
#         print("Balance:", self.__balance)


# account = Account("ACC101", 10000)
# account.display()

# output:
# Account Number: ACC101
# # Balance: 10000

# ===============================================================================================================================
# 11. Create a LibraryBook class with private __title and __issued. Add methods issue_book(),
# return_book(), and display_status().
# ================================================================================================================================
# class LibraryBook:
#     def __init__(self, title):
#         self.__title = title
#         self.__issued = False

#     def issue_book(self):
#         if not self.__issued:
#             self.__issued = True
#             print("Book issued")
#         else:
#             print("Book is already issued")

#     def return_book(self):
#         if self.__issued:
#             self.__issued = False
#             print("Book returned")
#         else:
#             print("Book was not issued")

#     def display_status(self):
#         print("Title:", self.__title)

#         if self.__issued:
#             print("Status: Issued")
#         else:
#             print("Status: Available")


# book = LibraryBook("Python Programming")

# book.display_status()
# book.issue_book()
# book.display_status()
# book.return_book()
# book.display_status()


# output:
# Book issued
# Title: Python Programming
# Status: Issued
# Book returned
# Title: Python Programming
# Status: Available

# ============================================================================================================================
# 12. Create a StudentResult class with private marks for three subjects. Add methods to calculate total,
# percentage, and grade.
# =============================================================================================================================
# class StudentResult:
#     def __init__(self, m1, m2, m3):
#         self.__m1 = m1
#         self.__m2 = m2
#         self.__m3 = m3

#     def total(self):
#         return self.__m1 + self.__m2 + self.__m3

#     def percentage(self):
#         return self.total() / 3

#     def grade(self):
#         percentage = self.percentage()

#         if percentage >= 90:
#             return "A"
#         elif percentage >= 75:
#             return "B"
#         elif percentage >= 60:
#             return "C"
#         elif percentage >= 40:
#             return "D"
#         else:
#             return "Fail"


# result = StudentResult(85, 90, 80)

# print("Total:", result.total())
# print("Percentage:", result.percentage())
# print("Grade:", result.grade())

# output:
# Total: 255
# Percentage: 85.0
# Grade: B

# ============================================================================================================
# 13. Create a Login class with private __username and __password. Add a method to validate login
# credentials.
# ==============================================================================================================
# class Login:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password

#     def validate_login(self, username, password):
#         if username == self.__username and password == self.__password:
#             print("Login successful")
#         else:
#             print("Invalid username or password")


# login = Login("admin", "1234")

# login.validate_login("admin", "1234")
# login.validate_login("admin", "1111")


# output:
# Login successful
# Invalid username or password


# ===========================================================================================================
# 14. Create a User class with private __email and __password. Provide methods to change the password
# only after checking the old password.
# ===========================================================================================================
# class User:
#     def __init__(self, email, password):
#         self.__email = email
#         self.__password = password

#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             print("Password changed successfully")
#         else:
#             print("Old password is incorrect")


# user = User("user@gmail.com", "1234")

# user.change_password("1234", "5678")
# user.change_password("1234", "9999")


# output:
# Password changed successfully
# Old password is incorrect

# =============================================================================================================================================
# 15. Create a Temperature class with private __celsius. Add methods to convert Celsius to Fahrenheit and
# Kelvin.
# ==============================================================================================================================================
# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius

#     def fahrenheit(self):
#         return (self.__celsius * 9 / 5) + 32

#     def kelvin(self):
#         return self.__celsius + 273.15


# temperature = Temperature(25)

# print("Fahrenheit:", temperature.fahrenheit())
# print("Kelvin:", temperature.kelvin())

# output:
# Fahrenheit: 77.0
# Kelvin: 298.15


# ==========================================================================================================
# 16. Create a BankCustomer class with private __name and __pin. Add a method to verify the PIN without
# exposing it directly.
# ============================================================================================================
# class BankCustomer:
#     def __init__(self, name, pin):
#         self.__name = name
#         self.__pin = pin

#     def verify_pin(self, pin):
#         if pin == self.__pin:
#             return True
#         else:
#             return False


# customer = BankCustomer("Bhumika", 1234)

# print(customer.verify_pin(1234))
# print(customer.verify_pin(1111))


# output:
# True
# False

# ==================================================================================================================================
# 17. Create an ATM class with private __balance and __pin. Implement deposit, withdraw, and balance
# inquiry using public methods.
# ===================================================================================================================================
# class ATM:
#     def __init__(self, balance, pin):
#         self.__balance = balance
#         self.__pin = pin

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Amount deposited")

#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0 and amount <= self.__balance:
#                 self.__balance -= amount
#                 print("Amount withdrawn")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Wrong PIN")

#     def balance_inquiry(self, pin):
#         if pin == self.__pin:
#             print("Balance:", self.__balance)
#         else:
#             print("Wrong PIN")


# atm = ATM(10000, 1234)

# atm.deposit(2000)
# atm.withdraw(3000, 1234)
# atm.balance_inquiry(1234)


# output:
# Amount deposited
# Amount withdrawn
# Balance: 9000

# ===================================================================================================================================
# 18. Create an Employee class with private __name, __department, and __salary. Add a method to
# calculate annual salary.
# ===================================================================================================================================
# class Employee:
#     def __init__(self, name, department, salary):
#         self.__name = name
#         self.__department = department
#         self.__salary = salary

#     def annual_salary(self):
#         return self.__salary * 12

#     def display(self):
#         print("Name:", self.__name)
#         print("Department:", self.__department)
#         print("Annual Salary:", self.annual_salary())


# employee = Employee("Rahul", "IT", 40000)
# employee.display()

# output:
# Name: Rahul
# Department: IT
# Annual Salary: 480000


# ================================================================================================================================
# 19. Create a HospitalPatient class with private __name, __age, and __bill. Add methods to add charges
# and display the bill.
# ================================================================================================================================
# class HospitalPatient:
#     def __init__(self, name, age, bill):
#         self.__name = name
#         self.__age = age
#         self.__bill = bill

#     def add_charges(self, amount):
#         if amount > 0:
#             self.__bill += amount

#     def display_bill(self):
#         print("Patient:", self.__name)
#         print("Age:", self.__age)
#         print("Bill:", self.__bill)


# patient = HospitalPatient("Amit", 30, 5000)

# patient.add_charges(2000)
# patient.display_bill()

# output:
# Patient: Amit
# Age: 30
# # Bill: 7000

# ===================================================================================================================================
# 20. Create a ShoppingCart class with private __items and __total. Add methods to add products, remove
# products, and calculate the total.
# ======================================================================================================================================
# class ShoppingCart:
#     def __init__(self):
#         self.__items = []
#         self.__total = 0

#     def add_product(self, name, price):
#         self.__items.append((name, price))
#         self.__total += price

#     def remove_product(self, name):
#         for item in self.__items:
#             if item[0] == name:
#                 self.__items.remove(item)
#                 self.__total -= item[1]
#                 print(name, "removed")
#                 return

#         print("Product not found")

#     def calculate_total(self):
#         return self.__total


# cart = ShoppingCart()

# cart.add_product("Laptop", 50000)
# cart.add_product("Mouse", 1000)

# print("Total:", cart.calculate_total())

# cart.remove_product("Mouse")

# print("Total:", cart.calculate_total())


# output:
# Total: 51000
# Mouse removed
# Total: 50000


# ============================================================================================================================================================
# 21. Create a Course class with private __course_name and __fees. Add validation so fees cannot be
# negative.
# ============================================================================================================================================================
# class Course:
#     def __init__(self, course_name, fees):
#         self.__course_name = course_name
#         self.__fees = 0
#         self.set_fees(fees)

#     def set_fees(self, fees):
#         if fees >= 0:
#             self.__fees = fees
#         else:
#             print("Fees cannot be negative")

#     def display(self):
#         print("Course:", self.__course_name)
#         print("Fees:", self.__fees)


# course = Course("Python", 5000)
# course.display()

# course.set_fees(-1000)

# output:
# Course: Python
# Fees: 5000
# Fees cannot be negative



# ===================================================================================================================================
# 22. Create a Vehicle class with private __fuel. Add methods refuel(), drive(), and show_fuel(). Prevent
# driving when fuel is insufficient.
# ===================================================================================================================================
# class Vehicle:
#     def __init__(self, fuel):
#         self.__fuel = fuel

#     def refuel(self, amount):
#         if amount > 0:
#             self.__fuel += amount

#     def drive(self, fuel_required):
#         if fuel_required <= self.__fuel:
#             self.__fuel -= fuel_required
#             print("Vehicle is driving")
#         else:
#             print("Insufficient fuel")

#     def show_fuel(self):
#         print("Fuel:", self.__fuel)


# vehicle = Vehicle(50)

# vehicle.drive(20)
# vehicle.show_fuel()

# vehicle.refuel(30)
# vehicle.show_fuel()

# vehicle.drive(100)


# output:
# Vehicle is driving
# Fuel: 30
# Fuel: 60
# Insufficient fuel


# =================================================================================================================================================
# 23. Create a Wallet class with private __money. Add add_money() and spend_money() methods with
# validation.
# ===================================================================================================================================================
# class Wallet:
#     def __init__(self, money):
#         self.__money = money

#     def add_money(self, amount):
#         if amount > 0:
#             self.__money += amount

#     def spend_money(self, amount):
#         if amount > 0 and amount <= self.__money:
#             self.__money -= amount
#             print("Money spent")
#         else:
#             print("Invalid amount or insufficient money")

#     def display(self):
#         print("Money:", self.__money)


# wallet = Wallet(1000)

# wallet.add_money(500)
# wallet.spend_money(300)
# wallet.display()

# output:
# Money spent
# Money: 1200


# ==================================================================================================================================
# 24. Create a Salary class with private __basic_salary. Add methods to calculate HRA, DA, and gross
# salary.
# =================================================================================================================================
# class Salary:
#     def __init__(self, basic_salary):
#         self.__basic_salary = basic_salary

#     def hra(self):
#         return self.__basic_salary * 0.20

#     def da(self):
#         return self.__basic_salary * 0.10

#     def gross_salary(self):
#         return self.__basic_salary + self.hra() + self.da()


# salary = Salary(30000)

# print("HRA:", salary.hra())
# print("DA:", salary.da())
# print("Gross Salary:", salary.gross_salary())


# output:
# HRA: 6000.0
# DA: 3000.0
# Gross Salary: 39000.0


# =======================================================================================================================================
# 25. Create a Result class with private __marks. Add a method to update marks only when the value is
# between 0 and 100.
# ========================================================================================================================================
# class Result:
#     def __init__(self, marks):
#         self.__marks = 0
#         self.update_marks(marks)

#     def update_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#             print("Marks updated")
#         else:
#             print("Marks must be between 0 and 100")

#     def display(self):
#         print("Marks:", self.__marks)


# result = Result(80)
# result.display()

# result.update_marks(95)
# result.display()

# result.update_marks(120)


# output:
# Marks updated
# Marks: 80
# Marks updated
# Marks: 95
# Marks must be between 0 and 100


# ==================================================================================================================================================
# 26. Create a DoorLock class with private __password. Add methods lock(), unlock(), and
# change_password().
# ==================================================================================================================================================
# class DoorLock:
#     def __init__(self, password):
#         self.__password = password
#         self.__locked = True

#     def lock(self):
#         self.__locked = True
#         print("Door locked")

#     def unlock(self, password):
#         if password == self.__password:
#             self.__locked = False
#             print("Door unlocked")
#         else:
#             print("Wrong password")

#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             print("Password changed")
#         else:
#             print("Wrong old password")


# door = DoorLock("1234")

# door.unlock("1234")
# door.lock()
# door.change_password("1234", "5678")


# output:
# Door unlocked
# Door locked
# Password changed


# =========================================================================================================================================
# 27. Create a Contact class with private __phone_number. Validate that the phone number contains exactly
# 10 digits before storing it.
# =========================================================================================================================================
# class Contact:
#     def __init__(self, phone_number):
#         self.__phone_number = ""
#         self.set_phone_number(phone_number)

#     def set_phone_number(self, phone_number):
#         if phone_number.isdigit() and len(phone_number) == 10:
#             self.__phone_number = phone_number
#         else:
#             print("Phone number must contain exactly 10 digits")

#     def display(self):
#         print("Phone:", self.__phone_number)


# contact = Contact("9876543210")
# contact.display()

# contact.set_phone_number("12345")

# output:
# Phone: 9876543210
# Phone number must contain exactly 10 digits


# ==================================================================================================================================================================================================
# 28. Create a Movie class with private __rating. Allow ratings only from 1 to 5.
# ==================================================================================================================================================================================================
# class Movie:
#     def __init__(self, rating):
#         self.__rating = 0
#         self.set_rating(rating)

#     def set_rating(self, rating):
#         if 1 <= rating <= 5:
#             self.__rating = rating
#         else:
#             print("Rating must be between 1 and 5")

#     def display(self):
#         print("Rating:", self.__rating)


# movie = Movie(4)
# movie.display()

# movie.set_rating(6)

# output:
# Rating: 4
# Rating must be between 1 and 5


# =========================================================================================================================================================
# 29. Create a Bank class with private __interest_rate. Add a method to calculate simple interest for a given
# principal and time.
# =========================================================================================================================================================
# class Bank:
#     def __init__(self, interest_rate):
#         self.__interest_rate = interest_rate

#     def simple_interest(self, principal, time):
#         return (principal * self.__interest_rate * time) / 100


# bank = Bank(5)

# print("Simple Interest:", bank.simple_interest(10000, 2))

# output:
# Simple Interest: 1000.0


# ==================================================================================================================================================
# 30. Create an Inventory class with private __quantity. Add stock and sell methods, preventing quantity from
# becoming negative.
# ==================================================================================================================================================
# class Inventory:
#     def __init__(self, quantity):
#         self.__quantity = quantity

#     def add_stock(self, quantity):
#         if quantity > 0:
#             self.__quantity += quantity

#     def sell(self, quantity):
#         if quantity > 0 and quantity <= self.__quantity:
#             self.__quantity -= quantity
#             print("Product sold")
#         else:
#             print("Insufficient stock")

#     def display(self):
#         print("Quantity:", self.__quantity)


# inventory = Inventory(50)

# inventory.add_stock(20)
# inventory.sell(30)
# inventory.display()

# inventory.sell(100)


# output:
# Product sold
# Quantity: 40
# Insufficient stock


# =======================================================================================================================================
# 31. Create a School class with private __school_name and __students. Add methods to add students and
# display the student count.
# =================================================================================================================================================
# class School:
#     def __init__(self, school_name):
#         self.__school_name = school_name
#         self.__students = []

#     def add_student(self, name):
#         self.__students.append(name)

#     def display_count(self):
#         print("School:", self.__school_name)
#         print("Student Count:", len(self.__students))


# school = School("ABC School")

# school.add_student("Amit")
# school.add_student("Rahul")
# school.add_student("Priya")

# school.display_count()


# output:
# School: ABC School
# Student Count: 3


# =======================================================================================================================================================
# 32. Create a Flight class with private __available_seats. Add booking and cancellation methods with proper
# validation.
# =========================================================================================================================================================
# class Flight:
#     def __init__(self, available_seats):
#         self.__available_seats = available_seats

#     def book(self, seats):
#         if seats > 0 and seats <= self.__available_seats:
#             self.__available_seats -= seats
#             print("Seats booked")
#         else:
#             print("Seats not available")

#     def cancel(self, seats):
#         if seats > 0:
#             self.__available_seats += seats
#             print("Booking cancelled")

#     def display(self):
#         print("Available seats:", self.__available_seats)


# flight = Flight(100)

# flight.book(5)
# flight.display()

# flight.cancel(2)
# flight.display()


# output:
# Seats booked
# Available seats: 95
# Booking cancelled
# Available seats: 97

# ========================================================================================================================================================================
# 33. Create a BusTicket class with private __passenger_name and __fare. Add methods to apply a discount
# and display the final fare.
# =========================================================================================================================================================================
# class BusTicket:
#     def __init__(self, passenger_name, fare):
#         self.__passenger_name = passenger_name
#         self.__fare = fare

#     def apply_discount(self, percentage):
#         if 0 <= percentage <= 100:
#             discount = self.__fare * percentage / 100
#             self.__fare -= discount

#     def display(self):
#         print("Passenger:", self.__passenger_name)
#         print("Final Fare:", self.__fare)


# ticket = BusTicket("Bhumika", 1000)

# ticket.apply_discount(10)
# ticket.display()


# output:
# Passenger: Bhumika
# Final Fare: 900.0


# ============================================================================================================================
# 34. Create a RestaurantBill class with private __amount. Add methods to add item prices, apply GST, and
# display the final bill.
# ================================================================================================================================
# class RestaurantBill:
#     def __init__(self):
#         self.__amount = 0

#     def add_item(self, price):
#         if price > 0:
#             self.__amount += price

#     def apply_gst(self, percentage):
#         gst = self.__amount * percentage / 100
#         self.__amount += gst

#     def display(self):
#         print("Final Bill:", self.__amount)


# bill = RestaurantBill()

# bill.add_item(500)
# bill.add_item(300)

# bill.apply_gst(18)

# bill.display()

# output:
# Final Bill: 944.0


# =======================================================================================================================
# 35. Create an ElectricityBill class with private __units. Calculate the bill using different rates for different
# unit ranges.
# ======================================================================================================================
# class ElectricityBill:
#     def __init__(self, units):
#         self.__units = units

#     def calculate_bill(self):
#         units = self.__units

#         if units <= 100:
#             bill = units * 5
#         elif units <= 200:
#             bill = (100 * 5) + ((units - 100) * 7)
#         else:
#             bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

#         return bill


# bill = ElectricityBill(250)

# print("Electricity Bill:", bill.calculate_bill())

# output:
# Electricity Bill: 1700


# ==================================================================================================================
# 36. Create a CreditCard class with private __limit and __used_amount. Prevent purchases that exceed the
# available limit.
# =====================================================================================================================
# class CreditCard:
#     def __init__(self, limit):
#         self.__limit = limit
#         self.__used_amount = 0

#     def purchase(self, amount):
#         if amount > 0 and self.__used_amount + amount <= self.__limit:
#             self.__used_amount += amount
#             print("Purchase successful")
#         else:
#             print("Purchase exceeds available limit")

#     def display(self):
#         print("Credit Limit:", self.__limit)
#         print("Used Amount:", self.__used_amount)


# card = CreditCard(50000)

# card.purchase(20000)
# card.purchase(40000)

# card.display()

# output:
# Purchase successful
# Purchase exceeds available limit
# Credit Limit: 50000
# Used Amount: 20000

# ===========================================================================================================================================================
# 37. Create a CourseRegistration class with private __student_name and __course. Add methods to
# register and display registration details.
# =========================================================================================================================================================
# class CourseRegistration:
#     def __init__(self, student_name, course):
#         self.__student_name = student_name
#         self.__course = course
#         self.__registered = False

#     def register(self):
#         self.__registered = True
#         print("Course registered")

#     def display(self):
#         print("Student:", self.__student_name)
#         print("Course:", self.__course)

#         if self.__registered:
#             print("Status: Registered")
#         else:
#             print("Status: Not Registered")


# registration = CourseRegistration("Bhumika", "Python")

# registration.register()
# registration.display()

# output:
# Course registered
# Student: Bhumika
# Course: Python
# Status: Registered



# ===============================================================================================================================================
# 38. Create a FreelanceProject class with private __client_name and __payment. Add a method to calculate
# payment after tax deduction.
# =================================================================================================================================================
# class FreelanceProject:
#     def __init__(self, client_name, payment):
#         self.__client_name = client_name
#         self.__payment = payment

#     def payment_after_tax(self, tax_percentage):
#         tax = self.__payment * tax_percentage / 100
#         return self.__payment - tax

#     def display(self):
#         print("Client:", self.__client_name)
#         print("Payment:", self.__payment)


# project = FreelanceProject("ABC Company", 50000)

# project.display()
# print("Payment after tax:", project.payment_after_tax(10))


# output:
# Client: ABC Company
# Payment: 50000
# Payment after tax: 45000.0


# ======================================================================================================================
# 39. Create a SalaryAccount class with private __balance. Add methods for credit, debit, and monthly
# interest calculation.
# =========================================================================================================================
# class SalaryAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def credit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def debit(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")

#     def monthly_interest(self, rate):
#         interest = self.__balance * rate / 100
#         self.__balance += interest

#     def display(self):
#         print("Balance:", self.__balance)


# account = SalaryAccount(30000)

# account.credit(5000)
# account.debit(2000)
# account.monthly_interest(1)

# account.display()


# output:
# Balance: 33330.0


# ===========================================================================================================================================
# 40. Create a SecureFile class with private __filename and __password. Add a method to open the file only
# after password verification.
# ============================================================================================================================================
# class SecureFile:
#     def __init__(self, filename, password):
#         self.__filename = filename
#         self.__password = password

#     def open_file(self, password):
#         if password == self.__password:
#             print("Opening file:", self.__filename)
#         else:
#             print("Wrong password")


# file = SecureFile("data.txt", "1234")

# file.open_file("1234")
# file.open_file("9999")

# output:
# Opening file: data.txt
# Wrong password


# =======================================================================================================================
# 41. Create a VotingSystem class with private __candidate_votes. Add methods to cast a vote and display
# vote counts.
# ============================================================================================================================
# class VotingSystem:
#     def __init__(self):
#         self.__candidate_votes = {}

#     def cast_vote(self, candidate):
#         if candidate in self.__candidate_votes:
#             self.__candidate_votes[candidate] += 1
#         else:
#             self.__candidate_votes[candidate] = 1

#     def display_votes(self):
#         for candidate, votes in self.__candidate_votes.items():
#             print(candidate, ":", votes)


# voting = VotingSystem()

# voting.cast_vote("A")
# voting.cast_vote("B")
# voting.cast_vote("A")
# voting.cast_vote("A")
# voting.cast_vote("B")

# voting.display_votes()

# output:
# A : 3
# B : 2