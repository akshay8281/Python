# 52. How can you pick a random item from a list or tuple?

# Using Random.choice()

import random

print("\n","*" * 60)

dataList = [1, 2, 3, 4, 5]

print("DataList Data : ",dataList,"\n")

choiceRandom = random.choice(dataList)

print("\nRandom Choice Method : ",choiceRandom)


