'''
11. Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''
def uniqueElements(inputList):
    uniqueList = []
    for element in inputList:
        if element not in uniqueList:
            uniqueList.append(element)
    return uniqueList

# Example usage
inputList = [1, 2, 2, 3, 4, 4, 5]
print(uniqueElements(inputList))






