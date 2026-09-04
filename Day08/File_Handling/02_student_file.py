# student.txt

file = open("student.txt", "w")

file.write("Name: Bhumika\n")
file.write("Age: 21\n")
file.write("City: Akluj")

file.close()

print("Student information saved successfully")

# output:
# Name: Bhumika
# Age: 21
# City: Akluj



# Take student name and marks from user
name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student_marks.txt", "w")

file.write("Name: " + name + "\n")
file.write("Marks: " + marks)

file.close()

print("Student information saved successfully")

# output:
# Student information saved successfully
# Enter student name: bhumika
# Enter marks: 80
# Student information saved successfully