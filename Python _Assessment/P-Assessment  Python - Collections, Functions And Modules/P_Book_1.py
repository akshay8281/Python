class Python_E_Book:
    def __init__(self):
        self.notes = []

    def generateNotes(self, name, title, content, filename):
        self.notes.append({'Name': name, 'Title': title, 'Content': content})
        print("\nNote Generated Successfully.")
   
        with open(filename, "a") as file:
            file.write("\nName : " + name + "\nTitle : " + title + "\nContent : " + content + "\n")

    def viewNotes(self):
        if not self.notes:
            print("Notes are not Available.")
            return
        index = 1
        for note in self.notes:
            print("\nNote " + str(index) + ": " + note['Name'])
            index += 1

        try:
            choice = int(input("\nEnter the note number you want to view: "))
            if 1 <= choice <= len(self.notes):
                note = self.notes[choice - 1]
                print("\nName: " + note['Name'])
                print("Title: " + note['Title'])
                print("Content: " + note['Content'])
            else:
                print("Invalid choice. Please enter a valid note number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")
