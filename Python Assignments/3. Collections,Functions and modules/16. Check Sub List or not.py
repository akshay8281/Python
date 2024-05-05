# 16. Write a Python program to check whether a list contains a sub list

def is_sublist(originalList, sublist):

    return all(item in originalList for item in sublist)


originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sublist = [4, 5, 6]

if is_sublist(originalList, sublist):
    print("Sublist found in the original List")
else:
    print("Sublist not found in the original List")









