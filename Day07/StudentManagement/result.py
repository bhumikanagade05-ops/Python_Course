def calculate_total(marks):

    return sum(marks)


def calculate_percentage(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def display_result(marks):

    total = calculate_total(marks)

    percentage = calculate_percentage(marks)

    grade = calculate_grade(percentage)

    print("\n----- RESULT -----")
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)