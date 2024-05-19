# 05. Write a Python program to read last n lines of a file.

file = open("sample.txt", "w")

file.write("My name is Akshay\n")
file.write("I live in Dholera\n")
file.write("I am studying Full Stack Developer Course\n")

file.close()
print("File Written Successfully")
print("")

file = open("sample.txt", "r")
lineNum = 1
lines = file.readlines()
lastLines = lines[-lineNum:]

for i in lastLines:
    print(i.strip())

file.close()








