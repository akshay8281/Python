'''
22. Write a Python function to reverses a string if its length is
a multiple of 4.
'''

userInput = input("Enter a string: ")

if len(userInput) % 4 == 0:
    reverseString = userInput[::-1]
    print("Reversed string:", reverseString)
else:
    print("String length is not a multiple of 4)
