# 4. Write a Python function to get the largest number,
# smallest num and sum of all from a list

numbers = [4,7,9,10,45,21,46,67,23]

big = numbers[0]
small = numbers[0]
sumTotal = 0

for num in numbers:
    if num > big:
        big = num
    if num < small:
        small = num
    sumTotal = sumTotal + num  

print("Biggest number is", big)
print("Smallest number is", small)
print("sumTotal of numbers is", sumTotal)








