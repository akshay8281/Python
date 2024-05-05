# 15. Write a Python program to get unique values from a list


def unique_values(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 4, 1, 2, 5, 6, 3, 7, 8, 9, 5]

unique_list = unique_values(input_list)

print("Original list:", input_list)
print("Unique values:", unique_list)
