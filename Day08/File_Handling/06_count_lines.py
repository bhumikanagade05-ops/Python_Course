# 6.Count number of lines
file = open("messages.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

file.close()

# output:
# Number of lines: 5