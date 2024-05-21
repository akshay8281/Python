# 37. Write a Python script to print a dictionary where the keys are
# numbers between 1 and 15


DictData = {}

for i in range(1, 16):
    DictData[i] = "Value " + str(i)

print("Keys and Values : \n\n", DictData)


