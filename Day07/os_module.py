# 15. Display Current Directory
# import os

# directory = os.getcwd()

# print("Current Working Directory:")
# print(directory)


# output:
# Current Working Directory:
# C:\Users\bhumi\Desktop\Python_Course\Day07



# --------------------------------------------------------------------------------------------
# 16. List Files and Folders
# ----------------------------------------------------------------------------------------------------
# import os

# items = os.listdir()

# print("Files and Folders:")

# for item in items:
#     print(item)


# output:
# Files and Folders:
# calculator.py
# main.py
# message.py
# operations.py
# os_module.py
# student.py
# __pycache__


# --------------------------------------------------------------------------------------------------
# 17. Create a Folder
# ------------------------------------------------------------------------------------------------
# import os

# folder_name = "student_data"

# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print("Folder created successfully.")
# else:
#     print("Folder already exists.")


# output:
# Folder created successfully.



# ------------------------------------------------------------------------------------------------------
# 18. Check File/Folder Exists
# ------------------------------------------------------------------------------------------------
# import os

# name = input("Enter file or folder name: ")

# if os.path.exists(name):
#     print("File or folder exists.")
# else:
#     print("File or folder does not exist.")


# OUTPUT:
# Enter file or folder name: student.py
# File or folder exists.   



 
