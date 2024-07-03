# First Method

num = [1,2,3,4,5,6,7,8,9]
print("\nMain List :",num)

square = [x**2 for x in num]

print("\nSquare of the List :",square)


# Second Method
numList = range(1,15)
print("\nNum List :",numList)

square2 = [y**2 for y in range(1,15)]

print("\nSquare of the List :",square2)


# using Function
l = []
for i in range(1,50):
    l.append(i**2)
print("\nLIST by Function :",l)

# Find Even Number
data = [i for i in range(11) if i % 2 == 0]
print("\nEven Number : ",data)

# Using Function
l1 = []
for i in range (11):
    if i % 2 == 0:
        l1.append(i)
print("Even Function",l1)
