# 24. Write a Python program to convert a list to a tuple.


ListData = [1, 2, 3, 4, 5]

tupleData = ()

for item in ListData:
    tupleData = tupleData + (item,) # if you want to create a tuple with a single item, you need to include a comma to ensure it is recognized as a tuple.

print("Convert List Data into Tuple Data :", tupleData)

print(type(tupleData))
