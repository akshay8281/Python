'''
11. Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''

def uniqueItems(lists):
    
    uniqueData = []
    
    for i in lists:
        if i not in uniqueData:
            uniqueData.append(i)
    return uniqueData
        
listItem = [1, 2, 3, 3,4,5,6,7,7,8,9,10]

uniqueValue = uniqueItems(listItem)

print("Original List:", listItem)
print("Unique Elements:", uniqueValue)
