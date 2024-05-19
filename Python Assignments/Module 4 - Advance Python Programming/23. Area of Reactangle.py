'''
23. Write a Python class named Rectangle constructed by a length and width
and a method which will compute the area of a rectangle
'''

class Rectangle:
    def Area_Rectangle(self, length, width):
        self.len = length
        self.wid = width

    def output(self):
        print("\nArea of Rectangle:", self.len * self.wid)

res = Rectangle()

len = float(input("Enter the length of the Rectangle : "))
wid = float(input("Enter the width of the Rectangle : "))

res.Area_Rectangle(len, wid)
res.output()






