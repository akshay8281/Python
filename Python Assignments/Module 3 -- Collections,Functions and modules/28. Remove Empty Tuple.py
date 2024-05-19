# 28. Write a Python program to remove an empty tuple(s) from a list of tuples.

tupleList = [(1, 2), (), (3, 4, 5), (), (), (6,), ()]


newTupleList = []


for data in tupleList:
    if data :
        newTupleList.append(data)

print("List after removing empty tuples : ", newTupleList)
