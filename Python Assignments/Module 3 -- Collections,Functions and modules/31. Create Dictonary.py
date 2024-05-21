# 31. How will you create a dictionary using tuples in python?

tuples = (('apple', 5), ('banana', 3), ('cherry', 8))

dictionary = dict(tuples)
dictData = {}

for key,value in tuples :
    dictData[key] = value

print(dictData)
print(type(dictData))


