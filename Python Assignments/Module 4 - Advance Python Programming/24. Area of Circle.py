'''
24. Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle
'''
PI = 3.14

class Circle:
    def setRadius(self, radius):
        self.rad = radius

    def computeArea(self):
        return PI * self.rad * self.rad
    
    def computePerimeter(self):
        return 2 * PI * self.rad

rad = float(input("\nEnter the radius of the circle: "))
c1 = Circle()
c1.setRadius(rad)
print("\nArea Of The Circle:", c1.computeArea())
print("\nPerimeter Of The Circle:", c1.computePerimeter())






