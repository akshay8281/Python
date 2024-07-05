class Calculator:
    def __init__(self):
        pass
    
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def display_menu(self):
        print("\n","*" * 35," Menu ","*" * 35,"\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit\n")

    def run_calculator(self):
        while True:
            self.display_menu()
            choice = input("Enter Your Choice (1 to 5): ")
            
            if choice == '5':
                print("\n\n","*"*20,"Exiting the calculator. Goodbye!","*"*20)
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("\nInvalid Choice. Please choose from 1 to 5.")
                input("Press Enter to continue....")
                continue
            
            try:
                num1 = float(input("\nEnter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                input("Press Enter to continue....")
                continue
            
            if choice == '1':
                result = self.addition(num1, num2)
                operation = "\nTotal Sum"
            elif choice == '2':
                result = self.subtraction(num1, num2)
                operation = "\nSubtraction"
            elif choice == '3':
                result = self.multiplication(num1, num2)
                operation = "\nMultiplication"
            elif choice == '4':
                result = self.division(num1, num2)
                operation = "\nDivision"
            

            if result == "Error! Division by zero.":
                print(result)
            else:
                print(operation + " = " + str(result))
            
            input("\n\nPress Enter to continue....")

if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()
