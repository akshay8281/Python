# 50. Write a Python function that checks whether a passed string is
# palindrome or not.

print("\n","*" * 60,"\n")

def isPalindrome(char):
    return char == char[::-1]
 
string = input("Enter a String : ")
output = isPalindrome(string)
 
if output:
    print("\n",string,": Yes,it is Palindroma")
else:
    print("\n",string,": No,it is Palindroma")

print("\n","*" * 60)

