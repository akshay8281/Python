# 4. Write a Python function to get the largest number,
# smallest num and sum of all from a list


l = [4,7,9,10,45,21,46,67,23]

larg = small = l[0]

for num in l:
    if num > larg:
        larg = num
    elif num < small:
        small = num

print("Largest:", larg)
print("Smallest:", small)






