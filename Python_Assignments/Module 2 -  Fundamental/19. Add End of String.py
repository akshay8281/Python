'''
19. Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with 'ing'
then add 'ly'instead if the string length of the given string is less than 3,
leave it unchanged.
'''
user = input("\nEnter a String : ")

if len(user) < 3:
    result = user
elif user.endswith('ing'):
    result = user + 'ly'
else:
    result = user + 'ing'

print(result)
