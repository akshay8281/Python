# 1. What is List? How will you reverse a list?

'''
In Python, a list is a collection of items, which can be of different types,
stored in a specific order. Lists are mutable, meaning their elements can be
changed after the list is created.


'''

# Through Reverse Method
print("\n*** Reverse Method ***\n")
reverse = [1,2,3,4,5,6,7,8,9,10]
reverse.reverse()
print(reverse)

# Slicing Method
print("\n\n*** Slicing Method ***\n")

sliceReverse = ["A","B","C","D","E"]
reverseMethod = sliceReverse [::-1]
print(reverseMethod)


