import EBook_1

        
while True :
    print("\n","*"*70,"\n")
    print("<"*12,"Welcome to Python E-Note Book",">"*12)
    print("\n1. Add Notes")
    print("2. View Notes")
    print("3. Exit\n")

    choice = int(input("Enter Your Choice : "))

    print("\n","*"*70,"\n")

    if choice == 1 :
        name = input("Enter your Name: ")
        title = input("\nEnter the note title: ")
        content = input("\nEnter the note content: ")
        EBook_1.generateNotes(name, title, content)

    elif choice == 2 :
            EBook_1.viewNotes()

    elif choice == 3 :
        print("*"*20,"Thank You For Using Our Services.","*"*20)
        break

    else :
        print("x"*20,"Invalid Choice.Please try again","x"*20)
           
