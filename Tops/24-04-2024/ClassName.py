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

