'''
25. What is Instantiation in terms of OOP terminology?
'''

class CarCompany:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def displayData(self):
        print(self.year,self.make,self.model)

car1 = CarCompany("Hyundia", "i 20", 2014)
car2 = CarCompany("Honda", "Amaze - Diesal", 2020)


car1.displayData()  
car2.displayData()  


'''
Class: Blueprint for creating objects.
Instantiation: Creating specific objects (car1, car2) from the class.
Object: An instance of the class with its own unique data.
'''
