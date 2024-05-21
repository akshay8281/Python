# 48. Write a Python function to check whether a number is in a given range


def RangeChecker():
    print("\n", "*" * 60)

    start = int(input("\nEnter Starting Range: "))
    end = int(input("Enter Ending Range: "))
    num = int(input("\nEnter a Number: "))

    for i in range(start, end + 1):
        if num == i:
            print("\n",num, "is in range")
            break
    else:
        print("\n",num, "is not in range")

    print("\n", "*" * 60)


RangeChecker()

