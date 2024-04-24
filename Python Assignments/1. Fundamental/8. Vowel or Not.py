'''
Qs 8 :- Write a Python program to test whether a passed letter is a
vowel or not.
'''

str = input("Enter a Character beyween A to Z :- ")

vowels = ["a","e","i","o","u","A","E","I","O","U"]

if str in vowels :
    print("It is vowel")
else :
    print("It is Consonent, not a Vowel")

