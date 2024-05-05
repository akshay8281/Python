# 52. How can you pick a random item from a list or tuple?

# Using Random.choice()

import random


print("\n","*" * 60)

dataList = [1, 2, 3, 4, 5]

print("DataList Data : ",dataList,"\n")

choiceRandom = random.choice(dataList)

print("\nRandom Choice Method : ",choiceRandom)


# Using random.randrange()

randomIndex = random.randrange(len(dataList))
randomRangeData = dataList[randomIndex]

print("\nRandom Range Method : ",randomRangeData)


# using random.sample

randomSample = random.sample(dataList, 1)
print("\nRandom Sample Method",randomSample)

print("\n","*" * 60)


