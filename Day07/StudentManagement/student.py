def add_student(data, roll_no, name, course):
    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": []
    }

    data.append(student)


def view_students(data):

    if len(data) == 0:
        print("No students found.")
        return

    print("\n----- STUDENT LIST -----")

    for student in data:

        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("------------------------")


def search_student(data, roll_no):

    for student in data:

        if student["roll_no"] == roll_no:
            return student

    return None


def delete_student(data, roll_no):

    for student in data:

        if student["roll_no"] == roll_no:
            data.remove(student)
            return True

    return False



# OUTPUT:
# ==============================
#    STUDENT MANAGEMENT SYSTEM
# ==============================
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Calculate Result
# 5. Delete Student
# 6. Exit
# Enter your choice: 1
# Enter Roll Number: 101
# Enter Student Name: bhumi
# Enter Course: DA
# Student added successfully.