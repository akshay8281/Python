# 06. Write a Python program to read a file line by line and store it into
# a list


filename = 'common.txt'
lines = []

file = open(filename, 'r')
for line in file:
    lines.append(line.strip())
file.close()

print(lines)









