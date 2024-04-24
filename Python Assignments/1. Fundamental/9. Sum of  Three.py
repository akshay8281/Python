'''
9. Write a Python program to sum of three given integers. However,
if two values are equal sum will be zero.
'''

print("\n*** Sum of Three Integers ***\n")

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

result = num1 + num2 + num3

if num1==num2 or num1==num3 or num2==num3 :
    result = 0
else :
    result = num1 + num2 + num3

print("\nThe Sum of Three is :",result)
    
