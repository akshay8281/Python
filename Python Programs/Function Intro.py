# Function with no Arguements and No Return Value

def printLine() :
    print("*" * 60)

printLine()
print("Welcome to User Defined Function Using Python.")
printLine()

# Function with Arguement with no return value

# Sum of User Input
def sum(a,b) :
    print("Sum : " , a+b)

printLine()
x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))

sum(x,y)
printLine()

# Sub of User input

def sub(a,b) :
    return a - b
printLine()
x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
# ans = sub(x,y)
# print("Subtraction :",ans)

print("Subtraction :",sub(x,y))
printLine()


