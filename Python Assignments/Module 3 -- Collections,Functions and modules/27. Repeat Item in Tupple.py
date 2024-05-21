# 27. Write a Python program to find the repeated items of a tuple.


tupleData = (1, 2, 3, 2, 4, 1.1, 5, 2, 6, 7, 8, 5, 10, 1.1)
repeatData = []

for i in range(len(tupleData)):
    if tupleData[i] in tupleData[:i]:
        if tupleData[i] not in repeatData:
            repeatData.append(tupleData[i])

print("Common Data are :", repeatData)


