# 40. Write a Python program to map two lists into a dictionary


code = [111,222,333,444,555,666,777]

print("\nCode Data : ",code,"\n")

items = ["Apple","Orange","Strawberry","Mango","Banana","Santra","Pineapple"]

print("Items Data : ",items)

mapData = {}

for i in range(len(code)):
   mapData[code[i]] = items[i]
 

print("\nMapData : \n",mapData)









