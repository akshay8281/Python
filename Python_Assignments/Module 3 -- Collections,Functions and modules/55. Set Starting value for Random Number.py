# 55. How will you set the starting value in generating random numbers?

import random

seedValue = int(input("\nEnter value : "))
random.seed(seedValue)

randomNum = random.randint(1, 10000)

print("\nRandom Number using seed for starting:", randomNum)
