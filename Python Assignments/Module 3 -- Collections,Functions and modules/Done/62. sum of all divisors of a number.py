# 62. Write a Python program to returns sum of all divisors of a number

print("\n","*" * 60,"\n")
print("<"*10,"Sum of All Divisors",">"*10)

num = int(input("\nEnter a number: "))
sum_divisors = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum_divisors += i
        
print("Sum of divisors:", sum_divisors)

print("\n","*" * 60,"\n")

