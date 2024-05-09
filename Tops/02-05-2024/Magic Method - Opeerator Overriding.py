
# magic Method
# Operator Overriding

class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        print("init Called X = ",x,"& Y = ",y)
    def __str__(self) :
        print("STR are Called")
        return "[{0},{1}]".format(self.x,self.y)
   

p1 = Point(10,20)
print(p1)
p2 = Point(30,40)
print(p2)



















