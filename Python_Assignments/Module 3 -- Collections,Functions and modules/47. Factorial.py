# 47. Write a Python function to calculate the factorial of a number
# (a nonnegative integer)


print("\n", "*" * 60)

def factNum(number):
    fact = 1
    for i in range(1,number + 1):
        fact = fact * i
    return fact
    
userFact = int(input("\nEnter the number : "))            
output = factNum(userFact)
print("\nUser Factorial Number : ",output)              


print("\n", "*" * 60)

