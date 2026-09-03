from datetime import datetime


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_time():

    return datetime.now().strftime("%H:%M:%S")


def calculate_age(birth_year):

    current_year = datetime.now().year

    return current_year - birth_year


def days_between_dates(date1, date2):

    first_date = datetime.strptime(date1, "%d-%m-%Y")
    second_date = datetime.strptime(date2, "%d-%m-%Y")

    difference = second_date - first_date

    return abs(difference.days)



# output:
# Current Date: 03-09-2026
# Current Time: 11:29:13
# Enter birth year: 2005
# Approximate Age: 21
# Enter first date (DD-MM-YYYY): 03-07-2005
# Enter second date (DD-MM-YYYY): 20-01-2007
# Days between dates: 566