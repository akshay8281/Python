# 07. Write a Python program to read a file line by line store it into a variable.


file = open("sample.txt","w")
file.write("Hello World")
file.write("Nice to Meet You All Of You.")
file.close()

location = 'common.txt'

file = open(location, 'r')
data = ""

for line in file:
    data.append(line.strip())

file.close()

for line in data:
    print(line)



