# Q1. Even or Odd Checker

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



#     output:Enter a number: 03
#            Odd



# Q2.Positive, Negative, or Zero

# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# output: Enter a number: 03
#         Positive



# Q3.Find Largest of Three Numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)




#     output:Enter first number: 03
#            Enter second number: 20
#            Enter third number: 05
#            Largest number is: 20




# Q4.Leap Year Checker

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "is a Leap Year")
# else:
#     print(year, "is not a Leap Year")


#     output: Enter a year: 2005
#             2005 is not a Leap Year





# Q5.Student Grading System

# marks = float(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 40:
#     print("Grade C")
# else:
#     print("Fail")


#     output:Enter marks: 95
#            Grade A+



# Q6.Voting Eligibility Checker
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to Vote")
# else:
#     years_left = 18 - age
#     print("You can vote after", years_left, "years")



# output:  Enter your age: 21
#         Eligible to Vote



# Q7.Discount Calculator


# bill = float(input("Enter total bill amount: "))

# if bill > 1000:
#     discount = bill * 20 / 100

# elif bill >= 500 and bill <= 1000:
#     discount = bill * 10 / 100

# else:
#     discount = 0

# final_amount = bill - discount

# print("Discount =", discount)
# print("Final Payable Amount =", final_amount)


# OUTPUT: Enter total bill amount: 10000
#         Discount = 2000.0
#        Final Payable Amount = 8000.0

