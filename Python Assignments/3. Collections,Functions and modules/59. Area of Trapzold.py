# 59. Write a Python program to calculate the area of a trapezoid


print("\n","*" * 60,"\n")

def AreaTrapzold(base1, base2, height):
    return (base1 + base2) * height / 2


base1 = float(input("Enter Base 1 value of Trapzold : "))
base2 = float(input("Enter Base 2 value of Trapzold : "))
height = float(input("Enter height value of Trapzold : "))

print("\nThe area of the trapezoid is:", AreaTrapzold(base1, base2, height))

print("\n","*" * 60)








