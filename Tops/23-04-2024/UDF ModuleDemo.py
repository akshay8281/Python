import UDF

print("*"*50)

print("1. oddEven")
print("2. maxOfTwo")
print("3. maxOfThree")
print("4. fibonacci")
print("5. prime")
print("6. pattern")
print("7. Exit")

while True :
    print("*"*50)

    choice = int(input("Enter a Value : "))

    if choice == 1 :
        a = int(input("\nEnter a Number : "))
        UDF.oddEven(a)
        print("*"*50)

    elif choice == 2 :
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        UDF.maxOfTwo(a,b)
        print("*"*50)

    elif choice == 3 :
        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))
        c = int(input("Enter Third Number : "))
        UDF.maxOfThree(a,b,c)
        print("*"*50)
    elif choice == 4 :
        n = int(input("Enter a Number : "))
        UDF.fibonacci(n)
        print("*"*50)
    elif choice == 5 :
        n = int(input("Enter a Number : "))
        UDF.prime(n)
        print("*"*50)

    elif choice == 6 :
        n = int(input("Enter a Number : "))
        UDF.pattern(n)
        print("*"*50)
    elif choice == 7 :
        print("Thank You For Using Our Services")
        print("*"*50)
        break
    else :
        print("Invalid Choice, Please Try Agian")
        print("*"*50)
    
    


