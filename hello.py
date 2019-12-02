import random

randNum = int(random.randrange(0, 50))
guess = False 
while guess == False :
    numberGuess = int(input("Guess the Number!"))
    if numberGuess == randNum :
        print(" you got it,don't give up!")
        checkCor = True 
    elif numberGuess > randNum :
        print("go lower boss")
    elif numberGuess < randNum:
        print("a bit higher boss")
if guess==randNum:
    print("thats whast up!!!")