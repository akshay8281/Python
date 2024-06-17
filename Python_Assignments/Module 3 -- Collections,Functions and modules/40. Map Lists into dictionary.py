# 40. Write a Python program to map two lists into a dictionary


code = [111, 222, 333, 444, 555, 666, 777]

print("\nCode Data:", code, "\n")

items = ["Apple", "Orange", "Strawberry", "Mango", "Banana", "Santra", "Pineapple"]

print("Items Data:", items)

mapData = {}

for i in range(len(code)):
    key = code[i]
    value = items[i]
    mapData[key] = value
   
print("\nMapData:\n", mapData)


