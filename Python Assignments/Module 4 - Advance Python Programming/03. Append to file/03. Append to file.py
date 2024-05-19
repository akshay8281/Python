# 03.Write a Python program to append text to a file and display the text.


sample = 'sample.txt'
appendText = input("\nEnter the text you want to append to the file: ")

file = open(sample, 'a')
file.write(appendText +'\n')
file.close()

file = open(sample, 'r')
content = file.read()

print("\nFile Content:\n\n", content)


file.close()
