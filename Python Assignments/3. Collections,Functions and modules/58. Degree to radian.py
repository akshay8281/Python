# 58. Write a Python program to convert degree to radian

print("\n","*" * 60)

def degToRadians(degrees):
    return degrees * (3.14159 / 180)

degrees = float(input("\nEnter a Degrees : "))

radians = degToRadians(degrees)

print("\n",degrees,"degrees is equal to",radians)

print("\n","*" * 60)
