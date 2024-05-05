# 32. Write a Python script to sort (ascending and descending) a
# dictionary by value.

import operator

dictonary = {'a': 2, 'b': 1, 'c': 3}

sortDictonary = dict(sorted(dictonary.items(), key=operator.itemgetter(1)))

print("\nDictonary Data are : ",dictonary)

print("\nSorted Data are : ",sortDictonary)


