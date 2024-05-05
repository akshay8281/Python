notes = []
    
def generateNotes(name,title,content) :    
    note = {"Name": name, "Title": title, "Content": content}
    notes.append(note)
try:
    file = open("notes.txt", "a")
    file.write(name,title,content)
    file.close()
except Exception as e:
    print("An error occurred: ",e)
    print("\nNote Generated Successfully:")


def viewNotes() :
    if not notes :
        print("Sorry, notes are not available!")
        return
    else:
        print("List of Exisiting Notes :\n")
        
        for i, note in enumerate(notes, start=1):
          print({i}, note['Title'])
          
        choice = input("\nEnter the number of the note you want to view: ")
        
        if not (1 <= int(choice) <= len(notes)):
            print("\n","x"*10,"Invalid input.","x"*10)
            return
        
    print("\nName :", notes[int(choice) - 1]['Name'])
    print("Title :", notes[int(choice) - 1]['Title'])
    print("Content :", notes[int(choice) - 1]['Content'])

try:
    with open("notes.txt", "r") as file:
        for line in file:
            name, title, content = line.strip().split(",")
            note = {"Name": name, "Title": title, "Content": content}
            notes.append(note)
except FileNotFoundError:
    pass
