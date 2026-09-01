# Q1.List Creation & Element Insertion

# numbers = []

# numbers.append(10)
# numbers.append(20)
# numbers.append(30)

# numbers.insert(1, 15)

# numbers.extend([40, 50])

# print(numbers)


# output:
# [10, 15, 20, 30, 40, 50]



# Q2. Element Removal & Retrieval

# items = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# items.remove("C++")

# last_item = items.pop()

# print("Modified List:", items)
# print("Last Item:", last_item)

# output:
# Modified List: ['Python', 'Java', 'JavaScript']
# Last Item: Ruby


# Q3. Element Frequency & Index Lookup

# scores = [85, 92, 75, 92, 88, 92, 70]

# count_92 = scores.count(92)

# index_88 = scores.index(88)

# print("Count of 92:", count_92)
# print("Index of 88:", index_88)

# output:
# Count of 92: 3
# Index of 88: 4



# Q4. Sorting & Reversing

# marks = [45, 89, 12, 67, 95, 34]

# marks.sort()

# print("Ascending:", marks)

# marks.reverse()

# print("Descending:", marks)

# output:
# Ascending: [12, 34, 45, 67, 89, 95]
# Descending: [95, 89, 67, 45, 34, 12]



# Q5. List Slicing Challenge

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print("First 5 elements:", arr[:5])

# print("Last 3 elements:", arr[-3:])

# print("Every second element from index 1 to 8:", arr[1:9:2])

# print("Reverse order:", arr[::-1])


# output:
# First 5 elements: [0, 1, 2, 3, 4]
# Last 3 elements: [7, 8, 9]
# Every second element from index 1 to 8: [1, 3, 5, 7]
# Reverse order: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



# Q6. Sum and Average of List Elements

# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# total = 0

# for num in numbers:
#     total = total + num

# average = total / len(numbers)

# print("Numbers:", numbers)
# print("Sum:", total)
# print("Average:", average)


# output:
# Enter a number: 20
# Enter a number: 03
# Enter a number: 05
# Enter a number: 06
# Enter a number: 56
# Numbers: [20, 3, 5, 6, 56]
# Sum: 90
# Average: 18.0


# Q7. Find Largest and Smallest Number


# def find_min_max(numbers):

#     maximum = numbers[0]
#     minimum = numbers[0]

#     for num in numbers:

#         if num > maximum:
#             maximum = num

#         if num < minimum:
#             minimum = num

#     return maximum, minimum


# numbers = [34, 12, 89, 5, 67]

# maximum, minimum = find_min_max(numbers)

# print("Max =", maximum)
# print("Min =", minimum)


# output:
# Max = 89
# Min = 5



# Q8. Remove Duplicates While Preserving Order

# numbers = [1, 3, 2, 3, 4, 1, 5, 2]

# unique_numbers = []

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# print(unique_numbers)


# output:
# [1, 3, 2, 4, 5]


# Q9. Separate Even and Odd Numbers


# numbers = [10, 15, 22, 33, 40, 55, 60]

# even_list = []
# odd_list = []

# for num in numbers:

#     if num % 2 == 0:
#         even_list.append(num)

#     else:
#         odd_list.append(num)

# print("Even:", even_list)
# print("Odd:", odd_list)


# output:
# Even: [10, 22, 40, 60]
# Odd: [15, 33, 55]



# Q10. Find the Second Largest Element Without Sorting


# numbers = [10, 45, 20, 99, 80, 99]

# largest = None
# second_largest = None

# for num in numbers:

#     if largest is None or num > largest:
#         second_largest = largest
#         largest = num

#     elif num != largest and (second_largest is None or num > second_largest):
#         second_largest = num

# print("Second Largest:", second_largest)


# output:
# Second Largest: 80



# Q11. List Comprehension – Square Only Odd Numbers


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = [num ** 2 for num in nums if num % 2 != 0]

# print(result)


# output:
# [1, 9, 25, 49, 81]



# Q12. Rotate List Left by K Positions


# def rotate_left(lst, k):

#     k = k % len(lst)

#     return lst[k:] + lst[:k]


# lst = [1, 2, 3, 4, 5]

# result = rotate_left(lst, 2)

# print(result)

# output:
# [3, 4, 5, 1, 2]



# Q13. Merge Two Sorted Lists

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8, 10]

# merged = []

# i = 0
# j = 0

# while i < len(list1) and j < len(list2):

#     if list1[i] < list2[j]:
#         merged.append(list1[i])
#         i += 1

#     else:
#         merged.append(list2[j])
#         j += 1


# while i < len(list1):
#     merged.append(list1[i])
#     i += 1


# while j < len(list2):
#     merged.append(list2[j])
#     j += 1


# print(merged)


# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 10]




# Q14. Flatten a Nested List Using Recursion


# def flatten(nested_list):

#     result = []

#     for item in nested_list:

#         if isinstance(item, list):
#             result.extend(flatten(item))

#         else:
#             result.append(item)

#     return result


# numbers = [1, [2, 3], [4, [5, 6]], 7]

# print(flatten(numbers))


# output:
# [1, 2, 3, 4, 5, 6, 7]



# Q15. Find Unique Pairs With Target Sum


# def find_pairs(nums, target):

#     pairs = []
#     seen = []

#     for num in nums:

#         required = target - num

#         if required in seen:
#             pair = (required, num)

#             if pair not in pairs:
#                 pairs.append(pair)

#         seen.append(num)

#     return pairs


# nums = [2, 4, 3, 5, 7, 8, 9]
# target = 7

# print(find_pairs(nums, target))


# output:
# [(4, 3), (2, 5)]


# Q16. Longest Consecutive Subsequence


# numbers = [100, 4, 200, 1, 3, 2]

# number_set = set(numbers)

# longest = 0

# for num in number_set:

#     if num - 1 not in number_set:

#         current_num = num
#         current_length = 1

#         while current_num + 1 in number_set:
#             current_num += 1
#             current_length += 1

#         if current_length > longest:
#             longest = current_length

# print("Longest sequence length:", longest)



# output:
# Longest sequence length: 4



# Q17. Group Anagrams

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# groups = {}

# for word in words:

#     key = "".join(sorted(word))

#     if key not in groups:
#         groups[key] = []

#     groups[key].append(word)

# result = list(groups.values())

# print(result)


# output:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



# Q18. Shallow Copy vs Reference


# a = [1, 2, [3, 4]]

# b = a.copy()

# b[0] = 99

# b[2][0] = 77

# print("a:", a)
# print("b:", b)


# output:
# a: [1, 2, [77, 4]]
# b: [99, 2, [77, 4]]


# Q19. Debugging – Removing Negative Numbers


# numbers = [-5, -2, 3, -4, -1, 6, 8]

# numbers = [num for num in numbers if num >= 0]

# print(numbers)


# output:
# [3, 6, 8]



# Q20. Matrix Transposition Using List Comprehension

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transpose = [
#     [matrix[row][col] for row in range(len(matrix))]
#     for col in range(len(matrix[0]))
# ]

# print(transpose)


# output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]




