# using Inheritence - Multiple
# Overriding Concept


class Base :
    def show(self):
        print("Show from base")
        
class Derived1(Base) :
    def show(self):
        super().show() # Third Call Dervide  2 bcs after call in sundervide first arguement than call dervide it make call second arguement of subdervide object
        print("Show from Derived 1")
        
class Derived2(Base) :
    def show(self):
        super().show() # call base class bcs base inheritence in dervide 2
        print("Show from Derived 2")
        
class SubDerived (Derived1,Derived2):
    def show(self):
       super().show() #second call Dervide 1 bcs only call first arguement in overriding
       print("Show from SubDerived") # First call Subdervide

s1 = SubDerived()
s1.show()

