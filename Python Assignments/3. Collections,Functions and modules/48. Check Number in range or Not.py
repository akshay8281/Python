# 48. Write a Python function to check whether a number is in a given range


print("\n", "*" * 60)

Start = int(input("\nEnter Starting Range : "))
End = int(input("Enter Ending Range : "))
num = int(input("\nEnter a Number : "))

is_in_range = False

for i in range(Start, End + 1):
    if num == i:
        is_in_range = True
        break

print(num, "is in range -", is_in_range)

print("\n", "*" * 60)
