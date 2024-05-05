# 34. Write a Python script to check if a given key already exists in a dictionary.


dictionary = {'apple': 3, 'banana': 1, 'cherry': 2}

keyCheck = input("Enter Key to check : ")

if keyCheck in dictionary:
    print(keyCheck,": key is exists in the dictionary.")
    
else:
    print(keyCheck,": key does not exist in the dictionary.")








