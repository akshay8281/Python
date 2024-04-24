'''
10. Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.
'''

num1 = int(input("\nEnter First Number: "))
num2 = int(input("Enter Second Number: "))

result = False
sub = 0
total = 0

if num1 == num2:
    result = True
elif num1 - num2 == 5:
    result = True
    sub = num1 - num2
elif num1 + num2 == 5:
    result = True
    total = num1 + num2
else:
    result = False

print("\nThe result is :", result)
print("The Subtraction of Num1 and Num2 is :", sub)
print("The Total of Num1 and Num2 is ", total)
