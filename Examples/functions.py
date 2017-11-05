
import random

def random_number(max_int):
    rand = random.randrange(0, max_int)
    print(rand)
    return rand

a_number = random_number(5)
print(a_number)




health = 10
 
roll_the_dice = random.randrange(1, 7) 
 
print("Health is " + str(health))

def hit_the_player():
    global health
    roll_the_dice = random.randrange(1,7)
    health -= roll_the_dice

hit_the_player()
print("Health is " + str(health)) 



print("Debug")


#Make the program below work, and print out two
#numbers multiplied together.

number_one = 3
x = random.randrange(0, 10)
num_two = x
times_two_numbers =(number_one*num_two)



 
print(times_two_numbers)
