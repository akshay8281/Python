# Prime Number

n = int(input("Enter a number : "))

if n%2==0 :
    for i in range (3, int(n/2) + 1, 2) :
        if n%1 == 0 :
            print(n,"is not a Prime Number")
    else :
        print(n, "is Prime")
else :
    print(n, "is not a prime")

