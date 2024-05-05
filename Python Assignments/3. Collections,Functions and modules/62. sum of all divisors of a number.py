# 62. Write a Python program to returns sum of all divisors of a number

print("\n","*" * 60,"\n")

print("<"*10,"Sum of All Divisors",">"*10)

def sum_of_divisors(number):
    
    divisors_sum = 0
    
    for i in range(1, number + 1):
        
        if number % i == 0:
            
            divisors_sum += i
            
    return divisors_sum


num = int(input("\nEnter a Number : "))

result = sum_of_divisors(num)

print("\nThe sum of divisors of ",num,"is :",result)

print("\n","*" * 60,"\n")

