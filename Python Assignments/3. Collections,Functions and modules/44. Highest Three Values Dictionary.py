# 44. Write a Python program to find the highest 3 values in a dictionary

def maxOfThree(a, b, c):
    values = {'a': a, 'b': b, 'c': c}
    maxValue = max(values.values())
    
    for key, value in values.items():
        if value == maxValue:
            print("\n",value, "is the largest number.")

# Example usage
print("\n","*"*60)
num1 = int(input("\nEnter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

maxOfThree(num1, num2, num3)

print("\n","*"*60)
