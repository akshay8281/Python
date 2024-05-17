from P_Book_1 import Python_E_Book

E_Book = Python_E_Book()


while True:

    print("\n", "*" * 70, "\n")
    print("<" * 12, "Welcome to Python E-Note Book", ">" * 12)
    print("\n1. Add Notes")
    print("2. View Notes")
    print("3. Exit")
    
    try:
        choice = int(input("\nEnter Your Choice : "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        continue

    print("\n", "*" * 70, "\n")

    if choice == 1:
        while True:
            name = input("Enter your Name: ")
            if name != "":
                break
            print("\nName cannot be empty. Please try again.")

        while True:
            title = input("\nEnter the note title: ")
            if title != "":
                break
            print("\nTitle cannot be empty. Please try again.")

        while True:
            content = input("\nEnter the note content: ")
            if content != "":
                break
            print("\nContent cannot be empty. Please try again.")
            
        E_Book.generateNotes(name, title, content, filename="Python_NoteBook.txt")

    elif choice == 2:
        E_Book.viewNotes()

    elif choice == 3:
        print("*" * 20, "Thank You For Using Our Services.", "*" * 20)
        break

    else:
        print("x" * 20, "Invalid Choice. Please try again", "x" * 20)
