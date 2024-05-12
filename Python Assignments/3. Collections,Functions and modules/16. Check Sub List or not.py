# 16. Write a Python program to check whether a list contains a sub list

originalList = [1,2,3,4,5,6,7,8,9]
sublist = [4,5,6]

for item in sublist:
    if item not in originalList:
        print("Sublist not found in the original List")
        break
else:
    print("Sublist found in the original List")





