'''
6. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
'''

def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage
string_list = ["abc", "xyz", "aba", "1221"]
result = count_strings(string_list)
print(f"Number of strings where the first and last character are the same: {result}")













