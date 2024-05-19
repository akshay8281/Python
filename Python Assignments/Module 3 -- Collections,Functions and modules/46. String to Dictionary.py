# 46. Write a Python program to create a dictionary from a string.

print("\n","*" * 60)
myStr = input("\nEnter a String : ")

dictionary = dict()
for char in myStr:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1
print("\nDictionary created from characters of the string is : \n")
print(dictionary)

print("\n","*" * 60)

