# 2. Write a Python program to get the Factorial number of given number


num = int(input("Enter a Number : "))

fact = 1

if num < 0:
   print("Factorial is not Possible below the Zero")
else:
   for i in range(1,num + 1):
       fact = fact * i
   print("The factorial of",num,"is",fact)
