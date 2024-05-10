import random

data = open("data.txt","w")
for i in range(10) :
    data.write(str(random.randint(1,100)) + ",")
data.close()

data = open("data.txt","r")
odd = open("odd.txt","w")
even = open("even.txt","w")
prime = open("prime.txt","w")

l = data.read().split(",")[:-1]
for i in l :
    if int(i)%2==0 :
        even.write(i + ",")
    elif (3, int(i/2) + 1, 2) :
        prime.write(i + ",")
    
    else :
        odd.write(i + ",")
        

data.close()
odd.close()
even.close()
prime.close()

print("Data File Content")
data = open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
data = open("even.txt","r")
print(data.read())
data.close()

print("Odd File Content")
data = open("odd.txt","r")
print(data.read())
data.close()

print("Prime File Content")
data = open("prime.txt","r")
print(data.read())
data.close()
