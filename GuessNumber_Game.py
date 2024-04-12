import random

#print(random.randint (1000,9999))
#print (random.choice ([1,20,90,True, "Aks"]))

num = random.randint(1,10)

while True :
    guess = int(input("Guess A number Between 1 To 20 : "))

    if guess==num :
        print("You Guessed A Correct Number")
        break
    elif guess>num :
         print("You Guessed A Greatest Number")
    elif guess<num :
         print("You Guessed A Smaller Number")
