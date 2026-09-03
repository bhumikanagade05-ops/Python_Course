# --------------------------------------------------------------------------------------
# 1. Create Your Own Module
# ----------------------------------------------------------------------------------------

# import calculator

# print("Addition =", calculator.add(10, 5))
# print("Subtraction =", calculator.subtract(10, 5))
# print("Multiplication =", calculator.multiply(10, 5))
# print("Division =", calculator.divide(10, 5))

# ---------------------------------------------------------------------------------------------
# 2. Import a Specific Function
# ---------------------------------------------------------------------------------------------



# from message import welcome

# welcome()



# ----------------------------------------------------------------------------------------------
# 3. Create a Student Module
# ----------------------------------------------------------------------------------------------


# from student import student_info

# student_info("Bhumika", 21, "DA")



# -----------------------------------------------------------------------------------------------
# 4. Use an Alias
# -----------------------------------------------------------------------------------------------


# import calculator as calc

# print("Addition =", calc.add(10, 20))
# print("Multiplication =", calc.multiply(10, 20))


# ----------------------------------------------------------------------------------------------------
# 5. Multiple Functions in a Module
# ----------------------------------------------------------------------------------------------------




# import operations

# print("Square =", operations.square(5))
# print("Cube =", operations.cube(5))
# print("Number is", operations.even_odd(5))

# --------------------------------------------------------------------------------------------------
# 6. Math Module
# ------------------------------------------------------------------------------------------------

# import math

# number = 25

# print("Square Root =", math.sqrt(number))
# print("Power =", math.pow(5, 2))
# print("Ceiling =", math.ceil(4.3))
# print("Floor =", math.floor(4.8))


# OUTPUT:
# Square Root = 5.0
# Power = 25.0
# Ceiling = 5
# Floor = 4


# ------------------------------------------------------------------------------------------------
# 7. Random Number Generator
# ----------------------------------------------------------------------------------------------
# import random

# number1 = random.randint(1, 100)
# number2 = random.randint(1, 10)

# print("Random number between 1 and 100:", number1)
# print("Random number between 1 and 10:", number2)


# OUTPUT:
# Random number between 1 and 100: 10
# Random number between 1 and 10: 6



# ---------------------------------------------------------------------------------------------------
# 8. Random OTP Generator
# --------------------------------------------------------------------------------------------------
# import random

# otp = random.randint(100000, 999999)

# print("Your OTP is:", otp)

# OUTPUT:
# Your OTP is: 541710



# ------------------------------------------------------------------------------------------------
# 9. Dice Simulator
# --------------------------------------------------------------------------------------------------
# import random

# dice = random.randint(1, 6)

# print("You rolled:", dice)


# OUTPUT:
# You rolled: 3



# ---------------------------------------------------------------------------------------------
# 10. Random Password Generator
# --------------------------------------------------------------------------------------------------
# import random
# import string

# characters = string.ascii_letters + string.digits

# password = ""

# for i in range(8):
#     password += random.choice(characters)

# print("Random Password:", password)


# OUTPUT:
# Random Password: FhysnxI8



# --------------------------------------------------------------------------------------------
# 11. Current Date and Time
# ----------------------------------------------------------------------------------------------
# from datetime import datetime

# current = datetime.now()

# print("Current Date and Time:", current)


# OUTPUT:
# Current Date and Time: 2026-09-03 10:15:34.614430



# -----------------------------------------------------------------------------------------
# 12. Display Current Date
# ---------------------------------------------------------------------------------------------
# from datetime import datetime

# today = datetime.now()

# print("Today's Date:", today.strftime("%d-%m-%Y"))


# OUTPUT:
# oday's Date: 03-09-2026


# ----------------------------------------------------------------------------------------------
# 13. Calculate Age
# -----------------------------------------------------------------------------------------------
# from datetime import datetime

# birth_year = int(input("Enter your birth year: "))

# current_year = datetime.now().year

# age = current_year - birth_year

# print("Approximate Age:", age)


# OUTPUT:
# Enter your birth year: 2005
# Approximate Age: 21

# ----------------------------------------------------------------------------------------------
# 14. Days Remaining
# --------------------------------------------------------------------------------------------------
# from datetime import datetime

# future_date = input("Enter future date (DD-MM-YYYY): ")

# future = datetime.strptime(future_date, "%d-%m-%Y")
# today = datetime.now()

# difference = future - today

# print("Days remaining:", difference.days)

# OUTPUT:
# Enter future date (DD-MM-YYYY): 21-12-2026
# Days remaining: 108



# -----------------------------------------------------------------------------------------------
# 19. Command-Line Arguments
# ---------------------------------------------------------------------------------------------------
# import sys

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])

# total = num1 + num2

# print("Sum =", total)





# -----------------------------------------------------------------------------------------------
# 20. Calculator Module + Menu
# -------------------------------------------------------------------------------------------------
# import calculator

# while True:

#     print("\n----- CALCULATOR -----")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "5":
#         print("Thank you!")
#         break

#     if choice in ["1", "2", "3", "4"]:

#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result =", calculator.add(a, b))

#         elif choice == "2":
#             print("Result =", calculator.subtract(a, b))

#         elif choice == "3":
#             print("Result =", calculator.multiply(a, b))

#         elif choice == "4":
#             print("Result =", calculator.divide(a, b))

#     else:
#         print("Invalid choice.")



 # ----------------------------------------------------------------------------------------------
# 21. Student Result Module
# -------------------------------------------------------------------------------------------------
# from student import calculate_total
# from student import calculate_percentage
# from student import calculate_grade

# marks = []

# for i in range(5):
#     mark = float(input(f"Enter marks for subject {i + 1}: "))
#     marks.append(mark)

# total = calculate_total(marks)
# percentage = calculate_percentage(marks)
# grade = calculate_grade(percentage)

# print("\n----- RESULT -----")
# print("Total Marks:", total)
# print("Percentage:", percentage)
# print("Grade:", grade)


# -----------------------------------------------------------------------------------------
# 22. Employee Module
# --------------------------------------------------------------------------------------------
# from employee import employee_details
# from employee import calculate_salary

# name = input("Enter employee name: ")
# employee_id = input("Enter employee ID: ")
# department = input("Enter department: ")

# basic = float(input("Enter basic salary: "))
# allowance = float(input("Enter allowance: "))
# bonus = float(input("Enter bonus: "))

# print("\n----- EMPLOYEE DETAILS -----")

# employee_details(name, employee_id, department)

# salary = calculate_salary(basic, allowance, bonus)

# print("Total Salary:", salary)



# ----------------------------------------------------------------------------------------
# 23. Bank Module
# ----------------------------------------------------------------------------------------
# import bank

# while True:

#     print("\n----- BANK MENU -----")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         amount = float(input("Enter deposit amount: "))
#         bank.deposit(amount)

#     elif choice == "2":

#         amount = float(input("Enter withdrawal amount: "))
#         bank.withdraw(amount)

#     elif choice == "3":

#         print("Current Balance:", bank.check_balance())

#     elif choice == "4":

#         print("Thank you for using the bank.")
#         break

#     else:

#         print("Invalid choice.")


# ----------------------------------------------------------------------------------------
# 24. Login Module
# --------------------------------------------------------------------------------------------
# from authentication import register_user
# from authentication import login_user

# while True:

#     print("\n----- LOGIN SYSTEM -----")
#     print("1. Register")
#     print("2. Login")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         if register_user(username, password):
#             print("Registration successful.")
#         else:
#             print("Username already exists.")

#     elif choice == "2":

#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         if login_user(username, password):
#             print("Login successful.")
#         else:
#             print("Invalid username or password.")

#     elif choice == "3":

#         print("Goodbye!")
#         break

#     else:

#         print("Invalid choice.")


# --------------------------------------------------------------------------------------------
# 25. Shopping Cart Module
# ---------------------------------------------------------------------------------------------
# import cart

# while True:

#     print("\n----- SHOPPING CART -----")
#     print("1. Add Product")
#     print("2. Remove Product")
#     print("3. Display Cart")
#     print("4. Calculate Total")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         name = input("Enter product name: ")
#         price = float(input("Enter price: "))
#         quantity = int(input("Enter quantity: "))

#         cart.add_product(name, price, quantity)

#         print("Product added.")

#     elif choice == "2":

#         name = input("Enter product name to remove: ")

#         cart.remove_product(name)

#     elif choice == "3":

#         cart.display_cart()

#     elif choice == "4":

#         print("Total = ₹", cart.calculate_total())

#     elif choice == "5":

#         print("Thank you!")
#         break

#     else:

#         print("Invalid choice.")











