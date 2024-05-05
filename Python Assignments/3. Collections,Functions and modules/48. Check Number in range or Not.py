# 48. Write a Python function to check whether a number is in a given range
print("\n","*" * 60)

def RangeNum(start,end,num):

    for i in range(start, end + 1):
        if num == i:
            return print(num,"is in range -",True)
    return print(num,"is not in range -",False)


Start = int(input("\nEnter Starting Range : "))
End = int(input("Enter Ending Range : "))
num = int(input("\nEnter a Number : "))

result = RangeNum(Start,End,num)

print(result)

print("\n","*" * 60)
