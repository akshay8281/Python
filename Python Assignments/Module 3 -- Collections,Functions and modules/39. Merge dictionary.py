# 39. Write a Python script to merge two Python dictionaries

print("*" * 60,"\n")

data1 = {"Akshay" : 888,"Nisha" : 777,"Jay":555,"Bhavin" : 444}
data2 = {"Mansi" : 101,"Niraj" : 123,"Ishant" : 789}

print("Data 1 : ",data1,"\n")
print("Data 2 : ",data2,"\n")


data1.update(data2)

print("Data Merge Data 1  and Data 2 : \n")
print(data1)


