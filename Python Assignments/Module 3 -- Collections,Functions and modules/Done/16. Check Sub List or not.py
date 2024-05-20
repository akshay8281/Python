# 16. Write a Python program to check whether a list contains a sub list

originalList = [1,2,3,4,5,6,7,8,9]
sublist = [4,5,6]

count = 0

for item in sublist:
    for orig_item in originalList:
        if item == orig_item:
            count = count + 1
            break

if count == len(sublist):
    print("Sublist found in the original List")
else:
    print("Sublist not found in the original List")


