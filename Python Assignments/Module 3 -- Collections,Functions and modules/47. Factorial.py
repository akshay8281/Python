# 47. Write a Python function to calculate the factorial of a number
# (a nonnegative integer)


print("\n", "*" * 60)

userNum = int(input("\nEnter a Number: "))

factorial = 1
if userNum < 0:
    result = "Negative integer, cannot find factorial."
elif userNum == 0 or userNum == 1:
    result = 1
else:
    for i in range(2, userNum + 1):
        factorial *= i
    result = factorial

print("\nFactorial of", userNum, "is", result)

print("\n", "*" * 60)

