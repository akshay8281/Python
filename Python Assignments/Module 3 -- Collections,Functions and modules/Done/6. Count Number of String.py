'''
6. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
'''

string_list = ["abc", "xyz", "aba", "1221"]

count = 0

for string in string_list:
    if string and string[0] == string[-1]:
        count += 1

print("The first and last character are the same: ", count)










