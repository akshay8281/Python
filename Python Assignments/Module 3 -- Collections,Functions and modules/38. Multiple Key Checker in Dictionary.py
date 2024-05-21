# 38. Write a Python program to check multiple keys exists in a dictionary

dataList = {123 : "kishan", 888 : "akshay", 222 : "bhavin", 777 : "jay"}

print("dataList : ",dataList,"\n")

keyChecker = {1,3,888}

print("keyChecker : ",keyChecker,"\n")

for key in keyChecker:
    if key in dataList:
        print(key,": key exists in the dictionary.")
    else:
        print(key,": key does not exist in the dictionary.")

