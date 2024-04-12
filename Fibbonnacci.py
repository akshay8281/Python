#Fibonacci number

# 0 1 1 2 3 ......
a , b=0,1
n = int (input("Enter a Number : "))
print(a, end=" ")
while b<n :
    print (b, end=" ")
    a, b=b, a+b
