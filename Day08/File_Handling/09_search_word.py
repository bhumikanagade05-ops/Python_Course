# Check whether a word exists
file = open("demo.txt", "r")

data = file.read()

word = input("Enter word to search: ")

if word in data:
    print("Word exists in the file")
else:
    print("Word does not exist in the file")

file.close()

# output:
# Enter word to search: Hello
# Word exists in the file