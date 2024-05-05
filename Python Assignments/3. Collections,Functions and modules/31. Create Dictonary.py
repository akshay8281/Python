# 31. How will you create a dictionary using tuples in python?
'''
tuples = (('apple', 5), ('banana', 3), ('cherry', 8))
dictionary = dict(tuples)
print(dictionary)
'''

tuples = (('apple', 5), ('banana', 3), ('cherry', 8))
dictionary = {key: value for key, value in tuples}
print(dictionary)





