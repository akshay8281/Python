# 4. Write a Python program to read first n lines of a file.


# Open the file for reading
file = open('common.txt', 'r')

n_line = 3

for line_number in range(n_line):
    line = file.readline().strip()
    if not line:
        print("no line")
        break
    print("\n", line)

file.close()







