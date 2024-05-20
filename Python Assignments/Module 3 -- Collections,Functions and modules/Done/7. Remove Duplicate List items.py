# 7. Write a Python program to remove duplicates from a list.

def uniqueValue(data):
    output = []
    for num in data:
        if num not in output:
            output.append(num)
    return output

listItems = [2, 4, 10, 20, 5, 2, 20, 4]
output = uniqueValue(listItems)

print("Final List Output :", output)
