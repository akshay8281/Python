'''
9. Write a Python function that takes two lists and returns true if
they have at least one common member
'''

list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

common = False
for data in list1:
    if data in list2:
        common = True
        break

print("Data which is Common : ", common)



