# 55. How will you set the starting value in generating random numbers?

import random

random.seed(int(input("Enter Seed value : ")))

print("Random Number using seed for starting :",random.randint(1, 10000))


