# 1. Take a name from the user and print it in uppercase

# name = input("Enter your name: ")

# print(name.upper())

# output:
# Enter your name: bhumii
# BHUMII


# 2. Take a name from the user and print it in lowercase

# name = input("Enter your name: ")

# print(name.lower())

# OUTPUT:
# Enter your name: BHUMII
# bhumii





# 3. Take a full name and print it in title case
# name = input("Enter your full name: ")

# print(name.title())

# output:
# Enter your full name: bhumika nagade
# Bhumika Nagade


# 4. Find the length of a string entered by the user

# text = input("Enter a string: ")

# print("Length =", len(text))


# output:
# Enter a string: Bhumika
# Length = 7



# 5. Print the first character of a string
# text = input("Enter a string: ")

# print("First character:", text[0])

# output:
# Enter a string: Bhumii
# First character: B


# 6. Print the last character of a string

# text = input("Enter a string: ")

# print("Last character:", text[-1])


# output:
# Enter a string: Bhumika
# Last character: a



# 7. Print the first three characters using slicing

# text = input("Enter a string: ")

# print("First three characters:", text[:3])


# output:
# Enter a string: Bhumika
# First three characters: Bhu


# 8. Reverse a string using slicing

# text = input("Enter a string: ")

# print("Reversed string:", text[::-1])


# output:
# Enter a string: Bhumii
# Reversed string: iimuhB




# 9. Count how many times the letter 'a' appears

# text = input("Enter a string: ")

# count = text.count("a")

# print("Number of a:", count)

# output:
# Enter a string: bhumika
# Number of a: 1



# 10. Replace 'Python' with 'Java'


# sentence = input("Enter a sentence: ")

# new_sentence = sentence.replace("Python", "Java")

# print(new_sentence)


# output:
# Enter a sentence: python is a programming language
# python is a programming language


# 11. Remove extra spaces from the beginning and end

# text = input("Enter a string: ")

# print(text.strip())


# output:
# Enter a string: bhumika nagade
# bhumika nagade


# 12. Check whether a word exists inside a sentence

# sentence = input("Enter a sentence: ")
# word = input("Enter a word to search: ")

# if word in sentence:
#     print("Word found")
# else:
#     print("Word not found")


# output:
# Enter a sentence: python is a programming language
# Enter a word to search: language
# Word found  




# 13. Take first name and last name and create a full name

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# full_name = first_name + " " + last_name

# print("Full Name:", full_name)


# output:
# Enter your first name: bhumika
# Enter your last name: nagade
# Full Name: bhumika nagade



# # 14. Use an f-string to display name, age and city

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")

# print(f"My name is {name}, I am {age} years old and I live in {city}.")


# output:
# Enter your name: bhumika
# Enter your age: 21
# Enter your city: akluj
# My name is bhumika, I am 21 years old and I live in akluj.


# 15. Check whether a string is empty or not

# text = input("Enter a string: ")

# if text == "":
#     print("String is empty")
# else:
#     print("String is not empty")


# output:
# Enter a string: bhumika
# String is not empty  



# 16. Check whether a string starts with a specific letter


# text = input("Enter a string: ")
# letter = input("Enter a letter: ")

# if text.startswith(letter):
#     print("The string starts with", letter)
# else:
#     print("The string does not start with", letter)


# output:
# Enter a string: bhumika
# Enter a letter: b
# The string starts with b



# 17. Check whether a string ends with .com

# website = input("Enter a website: ")

# if website.endswith(".com"):
#     print("The website ends with .com")
# else:
#     print("The website does not end with .com")


# output:
# Enter a website: google.com
# The website ends with .com



# 18. Count the number of vowels in a string


# text = input("Enter a string: ")

# count = 0

# for char in text.lower():
#     if char in "aeiou":
#         count += 1

# print("Number of vowels:", count)


# output:
# Enter a string: bhumika
# Number of vowels: 3


# 19. Count the number of words in a sentence


# sentence = input("Enter a sentence: ")

# words = sentence.split()

# print("Number of words:", len(words))


# output:
# Enter a sentence: python is a programming language
# Number of words: 5




# 20. Take an email address and display the username before @
email = input("Enter your email address: ")

# username = email.split("@")[0]

# print("Username:", username)

# output:
# Enter your email address: bhuminagade@gmail.com
# Username: bhuminagade











