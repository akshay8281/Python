
# Hierachy Level Inheritance

class A :
    def getA(self,a):
        self.a = a
    def putA(self):
        print("A : ",self.a)

class B(A) :
    def getB(self,b):
        self.b = b
    def putB(self):
        print("B : ",self.b)

class C(A) :
    def getC(self,c):
        self.c = c
    def putC(self):
        print("C : ",self.c)

class D(A) :
    def getD(self,d):
        self.d = d
    def putD(self):
        print("D : ",self.d)


b1 = B()
c1 = C()
d1 = D()

b1.getA(10)
b1.getB(200)
c1.getC(3000)
c1.getA(888)
d1.getD(40000)
d1.getA(454545)


b1.putA()
b1.putB()
c1.putC()
c1.putA()
d1.putD()
d1.putA()
