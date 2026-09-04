# Count number of words
file = open("messages.txt", "r")

data = file.read()

words = data.split()

print("Number of words:", len(words))

file.close()

# output:
# Number of words: 13