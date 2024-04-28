# User Define Function

# ODD Even Number
def oddEven(a):
    if a%2==0 :
        print(a,"is Even number")
    else :
        print(a,"is Odd number")

# Max number of two
def maxOfTwo (a,b) :
    if a>b :
        print(a,"is Max")
    else :
        print(b,"is Max")

# Max of Three
def maxOfThree(a,b,c):
    if a>b :
        if a>c:
            print(a,"is Max")
        else :
            print(c,"is Max")
    elif b>c :
        print(b,"is Max")
    else :
        print(c,"is Max")

# Fibonacci Series
def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n :
        print(b,end=" ")
        a,b=b,a+b
    print()

# Prime Number Check
def prime(n) :
    if n%2!=0:
        for i in range (3,int(n/2)+1,2) :
            if n%i==0 :
                print(n,"is not Prime")
                break
        else:
            print(n,"is Prime Number")
    else :
        print(n,"is not Prime Number")

# Patterns 
def pattern(n) :
    for i in range(1,n+1) :
        print("*" * i)


         





