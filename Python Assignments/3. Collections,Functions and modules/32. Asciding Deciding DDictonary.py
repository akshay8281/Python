# 32. Write a Python script to sort (ascending and descending) a
# dictionary by value.


numbers = [5, 2, 8, 1, 9, 3]

num_ascending = sorted(numbers)
print("\nSorted list Ascending :", num_ascending)

num_descending = sorted(numbers, reverse=True)
print("\nSorted list Descending :", num_descending)
