# 15. Write a Python program to get unique values from a list


List = [1, 2, 3, 4, 1, 2, 5, 6, 3, 7, 8, 9, 5]

uniqueItem = []

for item in List:
    if item not in uniqueItem:
        
        uniqueItem.append(item)

print("\nOriginal list:", List)
print("\nUnique values:", uniqueItem)
