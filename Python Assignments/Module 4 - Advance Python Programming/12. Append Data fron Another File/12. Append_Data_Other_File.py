# 12. Write a Python program to copy the contents of a file to another file.


company = open("main.txt", "r")
employee = open("subFile.txt", "a")

for content in company:
    employee.write(content)

company.close()
employee.close()

print("Contents of Company have been appended to Employee Successfully")

employee = open("subFile.txt", "r")

content = employee.read()

employee.close()

print("\nContents of subFile.txt are : ")
print(content)
