'''
9. Write a Python function that takes two lists and returns true if
they have at least one common member
'''


def commonNum(list1, list2):
    for i in list1:
        if i in list2:
            return print(True,": Both have common Number")
        else:
            return print(False,": Not Have ny Common Number")

list1 = [101,102,103,808,1001]
list2 = [111,222,333,888,101]


commonNum(list1,list2)

