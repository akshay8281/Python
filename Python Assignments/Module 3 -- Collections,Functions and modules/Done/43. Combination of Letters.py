'''
43. Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.

Sample data: {'1': ['a','b'], '2': ['c','d']}

Expected Output : ac ad bc bd

'''
print("*" * 60)
sampleData = {'1': ['a','b'], '2': ['c','d']}
print("Sample Data : ",sampleData)

ExpOutput = {"ac ad bc bd"}
print("Expected Output : ",ExpOutput)
print("*" * 60)


data = {'1': ['a', 'b'], '2': ['c', 'd']}

print("\nResult of Combinations : ")

for alpha1 in data['1']:
    for alpha2 in data['2']:
      
        print(alpha1 + alpha2,end=" ")

