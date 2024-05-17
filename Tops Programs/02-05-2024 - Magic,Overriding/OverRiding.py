# Overriding Method

class Base :
    def show(self):
        print("Show from base")
class Derived(Base) :
    def show(self):
        super().show()
        print("Show from Derived")
class SubDerived (Derived):
    def show(self):
        super().show()
        print("Show from SubDerived")

s1 = SubDerived()
s1.show()

