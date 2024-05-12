'''
11. Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''


userInput = [1, 2, 2, 3, 4, 4, 5]
uniqueList = []

for unique in userInput:
    if unique not in uniqueList:
        uniqueList.append(unique)

print(uniqueList)







