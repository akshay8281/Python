# 50. Write a Python function that checks whether a passed string is
# palindrome or not.

print("\n","*" * 60,"\n")

def isPalindrome(s):
    return s == s[::-1]
 

string = input("Enter a String : ")

result = isPalindrome(string)
 
if result:
    print("\n",string,": Yes,it is Palindroma")
else:
    print("\n",string,": No,it is Palindroma")

print("\n","*" * 60)







