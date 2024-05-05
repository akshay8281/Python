'''
45. Write a Python program to combine values in python list of dictionaries.

Sample data: [{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]

Expected Output:
Counter ({'item1': 1150, 'item2': 300})
'''


print("\n","*" * 60,"\n")

SampleData = [{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

print("Sample Data : ",SampleData)

ExpOutput = ({'item1': 1150, 'item2': 300})
print("\nExpected Output : ",ExpOutput)
print("\n","*" * 60,"\n")


result = {}

for data in SampleData:
    item = data['item']
    amount = data['amount']

    if item in result:
        result[item] = result[item] + amount

    else:
        result[item] = amount

print("*" * 60)
print("\nCombined data:")

for item, total in result.items():
    
    print("Item :" ,item, "Total amount : ", total)

print("*" * 60)
