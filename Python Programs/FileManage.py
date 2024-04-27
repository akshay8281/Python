file = open("tops1.txt","w")
file.write("This is File management Write Method")
file.close()
print("File Write Successfully")
print("**********************")

file = open("tops1.txt","r")
print(file.read())
#file.write("This is File management Read Method")
file.close()
print("File Read Successfully")
print("**********************")


file = open("tops1.txt","a")
file.write("This is File management Appended Method")
file.close()
print("File Appended Successfully")
print("**********************")

file = open("tops1.txt","r")
print(file.read())
file.close()


file = open("tops3.txt","w+")
file.write("This is Mode of W Plus Method")
print("Current File name : ",file.tell())
file.seek(0)
print("file Content",file.read())
file.close()
print("**********************")

