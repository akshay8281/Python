# 54. How can you get a random number in python?

import random

print("\n","*" * 10,"Get Random Number Methods","*" * 10)

# Using Random Randint
randomRandint = random.randint(1, 10)
print("\nRandom Randint Method : ",randomRandint)


# Using Random Float
randomFloat = random.random()
print("\nRandom Float Method : ",randomFloat)


# Using Random Float within range
randomFloatRange = random.uniform(100.00, 1000.00) 
print("\nRandom Float Method with Range : ", randomFloatRange)


# Using Suffle Method (Suffle Existing list Randomnly)

List = [1, 2, 3, 4, 5]

random.shuffle(List)
print("\nSuffle the List Randomnly : ",List)

print("\n","*" * 10,"Program End","*" * 10)







