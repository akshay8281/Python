# 14. Write a Python program to find the second smallest number in a list.

num = [12, 13, 1, 10, 34,5, 1]


if num[0] < num[1]:
    smallNum = num[0]
    secondSmallNum = num[1]
else:
    smallNum = num[1]
    secondSmallNum = num[0]


for currentNum in num[2:]:
    
    if currentNum < smallNum:
        secondSmallNum = smallNum
        smallNum = currentNum
        
    elif currentNum < secondSmallNum and currentNum != smallNum:
        secondSmallNum = currentNum

print("The second smallest number is :",secondSmallNum)
