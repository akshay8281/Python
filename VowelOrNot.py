# Define a string
string = input("Enter a String : ")

# Initialize a variable to store the count of vowels
vowel_count = 0

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

# Iterate over each character in the string
for char in string:
    # Check if the character is a vowel
    if char.lower() in vowels:
        vowel_count += 1

# Print the count of vowels in the string
print("The number of vowels in the string is:", vowel_count)
