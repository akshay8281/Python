# 30. Write a Python program to convert a list of tuples into a dictionary.

dataTupple = [('a', 1), ('b', 2), ('c', 3)]

result = {}

for key, value in dataTupple:
    result[key] = value

print("Dictionary Data:", result)


