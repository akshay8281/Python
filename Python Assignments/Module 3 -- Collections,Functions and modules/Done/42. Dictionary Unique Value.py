# 42. Write a Python program to print all unique values in a dictionary


def uniqueElements(inputData):
    
    uniqueList = []
    
    for value in inputData.values():
        
        if value not in uniqueList:
            
            uniqueList.append(value)
            
    return uniqueList

dictionaryData = {'Apple': 11, 'Mango': 20, 'Banana': 11, 'Pineapple': 31,
                  'Strawberry': 20}

uniqueData = uniqueElements(dictionaryData)

print("Unique Data in the dictionary are :", uniqueData)



