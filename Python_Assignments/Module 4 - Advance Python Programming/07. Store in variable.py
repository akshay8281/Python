# 07. Write a Python program to read a file line by line store it into a variable.

file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Nice to Meet You All Of You.\n")
file.close()

file = open("sample.txt", "r")
data = []

for line in file:
    data.append(line.strip())
file.close()

for line in data:
    print(line)




