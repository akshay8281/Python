'''
21. Write a Python function that takes a list of
words and returns the length of the longest one.
'''
string = input("Enter a String : ")

longest = 0
longest_word = ""

for word in string.split():
    if len(word) > longest:
        longest = len(word)
        longest_word = word

print("The longest word is", longest_word, "with length", len(longest_word))
