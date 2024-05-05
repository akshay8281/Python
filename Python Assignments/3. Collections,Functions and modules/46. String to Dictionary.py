# 46. Write a Python program to create a dictionary from a string.

print("\n","*" * 60)
myStr = input("\nEnter a String : ")

dictionary = dict()
for alpha in myStr:
    if alpha in dictionary:
        dictionary[alpha]+=1
    else:
        dictionary[alpha]=1
print("\nDictionary created from characters of the string is : \n")
print(dictionary)

print("\n","*" * 60)

