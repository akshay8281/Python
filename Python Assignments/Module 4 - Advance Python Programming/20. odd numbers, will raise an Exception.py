# 20. Write python program that user to enter only odd numbers,
# else will raise an exception.


try:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        print(num,"is an number")
    else:
        print(num,"is an Even number.Please enter an ODD Number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
