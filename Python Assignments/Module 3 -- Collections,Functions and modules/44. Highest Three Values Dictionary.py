# 44. Write a Python program to find the highest 3 values in a dictionary

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

values = {'a': num1, 'b': num2, 'c': num3}
maxValue = num1

for key, value in values.items():
    if value > maxValue:
        maxValue = value

print("\n", maxValue, "is the largest number.")
