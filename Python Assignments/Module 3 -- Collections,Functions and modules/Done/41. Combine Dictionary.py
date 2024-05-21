'''
41. Write a Python program to combine two dictionary adding values
for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

Counter = {}

print("*" * 60)

print("\nD1 Data : ",d1)
print("\nD2 Data : ",d2)
print("\nCounter Data : ",Counter)

for i in d1 :
    if i in d2 :
        Counter[i] = d1[i] + d2[i]
    else :
        Counter[i] = d1[i]

for i in d2 :
    if i not in d1 :
        Counter[i] = d2[i]

print("\n\nCounter Data after Merge and Sum of Common : \n",Counter)

print("\n","*" * 60)
