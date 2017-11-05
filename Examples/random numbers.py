import random

print ("Rolling the dice!")

print (random.randint(1, 12))



number = random.randint(0, 20)
isGuessed = False
count = 0

while (isGuessed == False and count <4):
    print ("Guesses Made: " + str(count))
    guess = input("Guess a number! ")

    guess = int(guess)
    if(guess == number):
        isGuessed = True
    elif(guess > number):
        print("Your guess is too high, try again!")
        count = count + 1
    elif(guess < number):
        print("Your guess is too low, try again!")
        count = count + 1
    else:
        count = count + 1

if(isGuessed == True):
    print("Congradulations!" + "\nYou guessed the number in " + str(count) + " tries!")
else:
    print("Sorry you didn't guess the number. ;-;")
    


