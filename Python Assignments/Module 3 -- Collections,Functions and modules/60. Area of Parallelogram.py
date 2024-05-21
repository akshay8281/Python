# 60. Write a Python program to calculate the area of a parallelogram

print("\n","*" * 60,"\n")

print("<"*10,"Area of Parallelogram",">"*10)

def AreaParallelogram(base, height):
    return base * height

base = float(input("\nEnter Base Value for Parallelogram : "))
height = float(input("\nEnter Hieght Value for Parallelogram : "))

result = AreaParallelogram(base, height)

print("\nThe area of the parallelogram is:", result)

print("\n","*" * 60)




