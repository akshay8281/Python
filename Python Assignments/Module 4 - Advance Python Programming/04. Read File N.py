# 4. Write a Python program to read first n lines of a file.


file = open("ReadLine.txt", "w")

file.write("Ancient Civilizations: India boasts one of the oldest civilizations in the world.\n")
file.write("Populous: India is the second-most populous country globally.\n")
file.write("Himalayan Majesty: The Himalayas border India to the north.\n")
file.write("Diverse: Unity in Diversity is India's motto, reflecting its cultural and religious variety.")
file.close()

print("File Written Successfully")

lineNum = 2


file = open('ReadLine.txt', 'r')

for para in range(lineNum):
    line = file.readline().strip()
    if not line:
        print("No Single lines are Available.")
        break
    print("\n", line)

file.close()







