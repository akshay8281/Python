class Bank :
    def openAccount(self,acNo,cName,balance) :
        self.acNo = acNo
        self.cName = cName
        self.balance = balance
        print("Hello ",self.cName,", Your Account Number ",str(self.acNo)," is ",str(self.balance) ," Rs.")

    def deposit(self,amount) :
        self.balance = self.balance + amount
    def withdraw (self, amount) :
        if amount<=self.balance :
            self.balance=self.balance-amount
        else :
            print("Your Current Balance is : ",self.balance)
    def checkBalance(self) :
        print("Your Current Balance is : ",self.balance)

b1 = Bank()
print("*"*60)
acNo =  int(input("Enter Account Number : "))
cName = input("Enter Customer Name : ")
balance = int(input("Enter Initial Balance : "))
print("*"*60,"\n")

b1.openAccount(acNo,cName,balance)
print("\n","*"*60)

while True :
    print("\n","*"*60)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*60,"\n")

    choice = int(input("Enter Yout Choice : "))
    print("\n","*"*60)

    if choice ==1 :
        amount= int(input("\nEnter Deposit Amount : "))
        b1.deposit(amount)
        print("\n","*"*60)
    elif choice == 2 :
        amount= int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("\n","*"*60)
    elif choice == 3 :
        
        b1.checkBalance()
        print("\n","*"*60)
    elif choice == 4 :
        print("Thank You For Using Our Services.")
        print("\n","*"*60)
        break
    else :
        print("Invalid Choice. Please Try Again. ")
        print("\n","*"*60)



        
