'''
10. Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''

Numsquares = []

for num in range(1, 31):
    Numsquares.append(num * num)

print("First 5 elements:")
print(Numsquares[:5])

print("\nLast 5 elements:")
print(Numsquares[-5:])

