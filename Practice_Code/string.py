'''
1. Generate Random Number from 1 to 100 (10 Numbers)
2. All Random Number Stored in mainData.txt
3. Find out Even Number from mainData.txt and stored in another file Even.txt and same as ODD Number stored in Odd.txt another file
4. 

'''

import random

data = open("mainData.txt","w")

for i in range(10):
    data.write(str(random.randint(1,100)) + ",")
data.close()