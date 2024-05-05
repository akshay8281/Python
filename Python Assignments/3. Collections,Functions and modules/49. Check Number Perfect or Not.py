# 49. Write a Python function to check whether a number is perfect or not.

print("\n","*" * 60)

num = int(input("\nEnter a Number : "))

def perfectNum(num):

    sum = 0
    
    for perfect in range(1, num):

        if num % perfect == 0:

            sum = sum + perfect
    
    return sum == num

result = perfectNum(num)

print(result) 

print("\n","*" * 60)
