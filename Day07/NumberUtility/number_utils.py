import math


def is_even(number):

    return number % 2 == 0


def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            return False

    return True


def factorial(number):

    if number < 0:
        return "Factorial not possible"

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


def reverse_number(number):

    return int(str(number)[::-1])


# output:
# Enter a number: 20
# Even: True
# Prime: False
# Factorial: 2432902008176640000
# Reverse: 2