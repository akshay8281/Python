# 63. Write a Python program to find the maximum and minimum numbers from the
# specified decimal numbers.


print("\n", "*" * 60, "\n")

print("<" * 10, "Max and Min from Decimal Numbers", ">" * 10)

decNumbers = [3.14, 10.20, 0.20, 8.8, 4.89, 2.718, 1.618, 4.669, 0.577]


if decNumbers:
    maxNum = decNumbers[0]
    minNum = decNumbers[0]

    for num in decNumbers[1:]:
        if num > maxNum:
            maxNum = num
        elif num < minNum:
            minNum = num

    print("\nThe Maximum Number is :", maxNum)
    print("\nThe Minimum Number is :", minNum)
else:
    print("\nThe list is empty.")

print("\n", "*" * 60, "\n")


