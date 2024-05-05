'''
10. Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''

l = [(i**2) for i in range(11, 25)]

print("First 5 elements:", l[:5])
print("Last 5 elements:", l[-5:])






