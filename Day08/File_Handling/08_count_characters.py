# Count number of characters
file = open("demo.txt", "r")

data = file.read()

print("Number of characters:", len(data))

file.close()


# output:
# Number of characters: 12