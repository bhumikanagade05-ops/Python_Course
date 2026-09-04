file = open("demo.txt", "w")

file.write("Hello Python")

file.close()

print("Data written successfully")

# output:
# Hello Python



# 15. Cities — write and append
file = open("cities.txt", "w")

file.write("Pune\n")
file.write("Mumbai\n")
file.write("Delhi\n")
file.write("Bangalore\n")
file.write("Chennai\n")

file.close()

file = open("cities.txt", "a")

file.write("Hyderabad\n")
file.write("Nashik\n")
file.write("Kolkata\n")

file.close()

print("City data saved successfully")