'''
9. Write a Python function that takes two lists and returns true if
they have at least one common member
'''


def has_common_member(lst1, lst2):
    for elem in lst1:
        if elem in lst2:
            return True
    return False

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print("Do the lists share any numbers?", has_common_member(list1, list2))




