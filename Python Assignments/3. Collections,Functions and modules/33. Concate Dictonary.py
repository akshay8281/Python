# 33. Write a Python script to concatenate following dictionaries
# to create a new one

data1 = {'Akshay': 111, 'Jay': 777}
data2 = {'Nisha': 333, 'Ishant': 666}
data3 = {'Bhavin': 444, 'Rajnikant': 888}
data4 = {'Jigar': 222, 'Komal': 999}

newData = {}

newData.update(data1)

newData.update(data2)

newData.update(data3)

newData.update(data4)

print(newData)

