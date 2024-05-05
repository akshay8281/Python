# 8. Write a Python program to check a list is empty or not.


def User(lis1): 
    if len(lis1) == 0: 
        return 0
    else: 
        return 1
  

lis1 = input("Please Enter Something : ") 
if User(lis1): 
    print("The list is not empty") 
else: 
    print("Empty List") 
