from student import (
    add_student,
    view_students,
    search_student,
    delete_student
)

from result import display_result

from validation import (
    validate_roll_no,
    validate_name,
    validate_marks
)


students = []


def add_new_student():

    roll_no = input("Enter Roll Number: ")

    if not validate_roll_no(roll_no):
        print("Invalid roll number.")
        return

    if search_student(students, roll_no):
        print("Roll number already exists.")
        return

    name = input("Enter Student Name: ")

    if not validate_name(name):
        print("Invalid name.")
        return

    course = input("Enter Course: ")

    add_student(
        students,
        roll_no,
        name,
        course
    )

    print("Student added successfully.")


def calculate_student_result():

    roll_no = input("Enter Roll Number: ")

    student = search_student(students, roll_no)

    if student is None:
        print("Student not found.")
        return

    marks = []

    print("\nEnter marks for 5 subjects:")

    for i in range(5):

        try:

            mark = float(
                input(f"Subject {i + 1}: ")
            )

            if not validate_marks(mark):

                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        except ValueError:

            print("Please enter a valid number.")
            return

    student["marks"] = marks

    display_result(marks)


def search_student_menu():

    roll_no = input("Enter Roll Number: ")

    student = search_student(
        students,
        roll_no
    )

    if student:

        print("\n----- STUDENT FOUND -----")

        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Course:", student["course"])

        if student["marks"]:

            display_result(student["marks"])

    else:

        print("Student not found.")


def delete_student_menu():

    roll_no = input("Enter Roll Number: ")

    if delete_student(students, roll_no):

        print("Student deleted successfully.")

    else:

        print("Student not found.")


while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_new_student()

    elif choice == "2":

        view_students(students)

    elif choice == "3":

        search_student_menu()

    elif choice == "4":

        calculate_student_result()

    elif choice == "5":

        delete_student_menu()

    elif choice == "6":

        print("Thank you for using Student Management System.")
        break

    else:

        print("Invalid choice. Please try again.")