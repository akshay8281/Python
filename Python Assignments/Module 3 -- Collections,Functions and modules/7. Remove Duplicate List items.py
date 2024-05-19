# 7. Write a Python program to remove duplicates from a list.

  
listData = [2, 4, 10, 20, 5, 2, 20, 4]
result = []

for num in listData:
    if num not in result:
        result.append(num)

print("Final List are : ",result)














