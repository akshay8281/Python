# 15. Write a Python program to count occurrences of a substring in a string.

def count_substring_occurrences(string, substring):
    return string.count(substring)

# Example usage
string = input("Enter a String to calculate Sub String : ")

substring = input("Enter Sub String : ")
count = count_substring_occurrences(string, substring)
print("Number of occurrences of ",substring ,' in ',string ,":", count)
