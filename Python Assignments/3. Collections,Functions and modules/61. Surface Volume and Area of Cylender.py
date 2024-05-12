# 61. Write a Python program to calculate surface volume and area of a cylinder

print("\n","*"*60,"\n")

print("<"*7,"Calculation of Surface Volume And Area Of A Cylinder",">"*7)


def Area_of_SC(radius, height):
    return 2 * 3.14 * radius * (radius + height)

def Cylinder_Volume(radius, height):
    return 3.14 * radius * radius * height


radius = float(input("\nEnter Radius of Cylinder : "))
height = float(input("\nEnter Height of Cylinder : "))

surfaceArea = Area_of_SC(radius, height)
volume = Cylinder_Volume(radius, height)

print("\nSurface Area of Cylinder are :", surfaceArea)
print("\nVolume:", volume)

print("\n","*"*60,"\n")
