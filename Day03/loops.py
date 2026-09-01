# 1. Print numbers from 1 to 10 using a for loop

# for i in range(1, 11):
#     print(i)


# output: 1
#         2
#         3
#         4
#         5
#         6
#         7
#         8
#         9
#        10



# 2. Print numbers from 1 to 100

# for i in range(1, 101):
#     print(i)


# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59
# 60
# 61
# 62
# 63
# 64
# 65
# 66
# 67
# 68
# 69
# 70
# 71
# 72
# 73
# 74
# 75
# 76
# 77
# 78
# 79
# 80
# 81
# 82
# 83
# 84
# 85
# 86
# 87
# 88
# 89
# 90
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99
# 100



# 3. Print all even numbers between 1 and 50

# for i in range(2, 51, 2):
#     print(i)



# output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28
# 30
# 32
# 34
# 36
# 38
# 40
# 42
# 44
# 46
# 48
# 50    



# 4. Print all odd numbers between 1 and 50


# for i in range(1, 51, 2):
#     print(i)

# output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29
# 31
# 33
# 35
# 37
# 39
# 41
# 43
# 45
# 47
# 49    



# 5. Print numbers from 10 to 1 in reverse order
# for i in range(10, 0, -1):
#     print(i)

# output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1



# 6. Print the multiplication table of a number entered by the user

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# output:
# Enter a number: 101
# 101 x 1 = 101
# 101 x 2 = 202
# 101 x 3 = 303
# 101 x 4 = 404
# 101 x 5 = 505
# 101 x 6 = 606
# 101 x 7 = 707
# 101 x 8 = 808
# 101 x 9 = 909
# 101 x 10 = 1010    


# 7. Find the sum of numbers from 1 to 100
import numbers


total = 0

# for i in range(1, 101):
#     total = total + i

# print("Sum =", total)

# output:
# Sum = 5050


# 8. Find the sum of all even numbers from 1 to 100


total = 0

# for i in range(2, 101, 2):
#     total = total + i

# print("Sum =", total)

# output:Sum = 2550



# 9. Find the factorial of a number using a loop

# num = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, num + 1):
#     factorial = factorial * i

# print("Factorial =", factorial)


# output:
# Enter a number: 25
# Factorial = 15511210043330985984000000




# 10. Count how many numbers are present between 1 and a user-entered number


# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     count = count + 1

# print("Total numbers =", count)


# output:
# Enter a number: 100
# Total numbers = 100


# 11. Print numbers divisible by 5 between 1 and 100

# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)

# output:
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
# 100  



# 12. Use a while loop to print numbers from 1 to 20
# i = 1

# while i <= 20:
#     print(i)
#     i = i + 1

# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20   


# 13. Use a while loop to print even numbers from 2 to 20

# i = 2

# while i <= 20:
#     print(i)
#     i = i + 2


#   output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20  



# 14. Keep printing numbers and stop when the number becomes 5 using break

# for i in range(1, 11):
#     if i == 5:
#         break

#     print(i)

# output:
# 1
# 2
# 3
# 4    


# 15. Print numbers from 1 to 10 but skip 5 using continue

# for i in range(1, 11):
#     if i == 5:
#         continue

#     print(i)

# output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10



# 16. Find the sum of the first N natural numbers

# n = int(input("Enter N: "))

# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum =", total)

# output:
# Enter N: 100
# Sum = 5050



# 17. Calculate the power of a number without using the ** operator
# base = int(input("Enter base: "))
# power = int(input("Enter power: "))

# result = 1

# for i in range(power):
#     result = result * base

# print("Result =", result)


# output:
# Enter base: 20
# Enter power: 30
# Result = 1073741824000000000000000000000000000000



# 18. Print the first 10 multiples of 3

# for i in range(1, 11):
#     print(3 * i)


# output:
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30  




# 19. Count numbers between 1 and 100 divisible by both 2 and 5

# count = 0

# for i in range(1, 101):
#     if i % 2 == 0 and i % 5 == 0:
#         count = count + 1

# print("Count =", count) 

# output:
# Count = 10  


# 20. Create a simple menu loop that repeats until the user enters 0

# choice = -1

# while choice != 0:
#     print("\n--- MENU ---")
#     print("1. Say Hello")
#     print("2. Say Welcome")
#     print("0. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Hello!")

#     elif choice == 2:
#         print("Welcome!")

#     elif choice == 0:
#         print("Program exited successfully.")

#     else:
#         print("Invalid choice. Please try again.")


# output:
# --- MENU ---
# 1. Say Hello
# 2. Say Welcome
# 0. Exit
# Enter your choice: -1
# Invalid choice. Please try again.

# --- MENU ---
# 1. Say Hello
# 2. Say Welcome
# 0. Exit
# Enter your choice:         







 
  



   