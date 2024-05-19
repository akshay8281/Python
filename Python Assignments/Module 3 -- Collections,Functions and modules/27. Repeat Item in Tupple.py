# 27. Write a Python program to find the repeated items of a tuple.

data = (1,2,3,2,4,1.1,5,2,6,7,8,5,10,1.1)
repeatData = []
checkData = []

for item in data:
    if item in checkData:
        if item not in repeatData:
            repeatData.append(item)
    else:
        checkData.append(item)

print("Repeated Data are:", repeatData)









