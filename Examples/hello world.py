name=" "
name=input("enter your name")
print("hello", name)
if name=="Dylan":
    print("Cool Name!!!")
elif name=="Joe":
    print("Okay name")
else:
    print("eh...")

numArray = [1,2,3,4,5,6,7,8,9,10]
for item in numArray:
    print(item)

x=0
while x < 10:
    print("Hello!")
    x = x+1

guessed = False
while guessed == False:
    guess = input ("Guess a number!")
    if int(guess)==7:
        guessed = 7

print ("You win!")

