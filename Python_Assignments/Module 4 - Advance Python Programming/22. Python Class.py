# 22. How to Define a Class in Python? What Is Self?
# Give An Example Of A Python Class

'''
How to Define a Class in Python?
>> Define a class in Python with "class" ClassName:
    Class is group of different type variables and functions.

>> What Is Self?
self in a Python class refers to the instance of the class. It allows access
to the class's attributes and methods from within the class methods.

>> Give An Example Of A Python Class :
'''

class Student : 
    def getData(self,fName,lName) :
        print("getData Called")
        self.f = fName
        self.l = lName
    def putData(self) :
        print("PutData Called")
        print("First Name : ",self.f)
        print("Last Name : ",self.l)
        
s1 = Student()
s1.getData("Akshay","Pitroda")
s1.putData()
