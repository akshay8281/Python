# 27. Write a Python program to find the repeated items of a tuple.

def findRepeatData(data):
    repeatData = []
    checkData = []
    
    for item in data:
        if item in checkData and item not in repeatData:
            repeatData.append(item)
        else:
            checkData.append(item)
    
    return repeatData

data = (1,2,3,2,4,1.1,5,2,6,7,8,5,10,1.1)

repeatData = findRepeatData(data)

print("Repeated Data are :", repeatData)









