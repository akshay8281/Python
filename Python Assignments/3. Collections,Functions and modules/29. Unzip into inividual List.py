 # 29. Write a Python program to unzip a list of tuples into individual lists.


tupleList = [(1, 2), ("Akshay","Pitroda"),(3, 4), (8, 9)]

data_1 = []
data_2 = []


for element in tupleList:
    data_1.append(element[0])
    data_2.append(element[1])


print("First elements:", data_1)
print("Second elements:", data_2)

