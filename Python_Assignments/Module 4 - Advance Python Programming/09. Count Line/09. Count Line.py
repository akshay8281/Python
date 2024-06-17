# 09. Write a Python program to count the number of lines in a text file


file = open("sample.txt","w")

file.write("High-Level: Python is a high-level programming language.\n")
file.write("Interpreted: Python is an interpreted language\n")
file.write("Dynamically Typed : No need to declare variable types.\n")
file.write("Readable Syntax: Emphasizes readability and simplicity.\n")
file.write("Readable Syntax: Emphasizes readability and simplicity.\n")

file.close()
print("File Written Successfully\n")


file = open("sample.txt", "r")
count = 0
for i in file:
    count = count + 1

print("Number of lines in the file:", count)





