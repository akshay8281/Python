# 38. Write a Python program to check multiple keys exists in a dictionary

dataList = {"kishan": 123, "akshay": 888, "bhavin": 222, "jay": 777}

print("dataList : ",dataList,"\n")

keyChecker = {"akshay", "apple", "fruity"}

print("keyChecker : ",keyChecker,"\n")

for key in keyChecker:
    if key in dataList:
        print(key,": key exists in the dictionary.")
    else:
        print(key,": key does not exist in the dictionary.")

