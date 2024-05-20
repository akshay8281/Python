# 17. Write a Python program to split a list into different variables

lists = [1,2,3,4,5,6,7,8]

data1 = lists[:4]  
data2 = []

for item in lists[4:]:
    data2.append(item)

print(data1)
print(data2)
