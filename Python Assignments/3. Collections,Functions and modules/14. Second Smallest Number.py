# 14. Write a Python program to find the second smallest number in a list.


def second_smallest(numbers):

    smallest = min(numbers)

    numbers.remove(smallest)

    second_smallest = min(numbers)
    
    return second_smallest

numbers = [1, 2, 3, 10, 15, 0, 25, 6]

result = second_smallest(numbers)

print("Second smallest number:", result)



