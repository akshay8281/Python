# 11. Write a Python program to write a list to a file.


data = ["Akshay","Jay","Nisha","Aarohi","Bhavin"]

file = open("test.txt", "w")

for item in data:
    file.write(item + "\n")
    
file.close()

print("Data has been written to file")
print("Data Written Successfully")


file = open("test.txt", "r")

fileData = file.read()

file.close()

print("\nData in the File : \n")
print(fileData)










