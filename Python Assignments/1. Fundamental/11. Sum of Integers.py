# 11. Write a python program to sum of the first n positive integers.

sum = 0

num = int(input("Enter a Number : "))

while num>0 :
    sum = sum + num
    num = num - 1
print("Sum of Integers is : ", sum)

