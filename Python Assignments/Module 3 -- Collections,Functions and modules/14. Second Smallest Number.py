# 14. Write a Python program to find the second smallest number in a list.


numList = [1,50,3,10,15,0,25,6]


small = numList[0]
second_small = numList[1]


for num in numList[2:]:
    if num < small:
        second_small = small
        small = num
    elif num < second_small:
        second_small = num

print("Second smallest number:", second_small)
