# 47. Write a Python function to calculate the factorial of a number
# (a nonnegative integer)
print("\n","*" * 60)

userNum = int(input("\nEnter a Number: "))

def factorial(n):
    if n < 0:
        return "Negative integer,cannot Factorial og given Number."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(userNum)
print("\nFactorial of",userNum,"is",result)

print("\n","*" * 60)

