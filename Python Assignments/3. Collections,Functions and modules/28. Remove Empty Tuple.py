# 28. Write a Python program to remove an empty tuple(s) from a list of tuples.

List = [(),(),(1,2),(),(True,False),(),("a","b","c","d"),()]

List = [tupple for tupple in List if tupple]

print("List Items : \n",List) 
