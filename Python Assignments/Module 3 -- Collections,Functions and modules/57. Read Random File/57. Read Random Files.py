#57. Write a Python program to read a random line from a file.

import random

file = open("sample.txt", 'r')
lines = file.readlines()
file.close()

if lines:
    randomLines = random.choice(lines).strip()
    print("Random line from the file:")
    print(randomLines)
else:
    print("The file is empty.")
