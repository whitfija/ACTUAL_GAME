list_of_numbers = [0,4,5,9,7,8,1,2,6,3]
list_of_strings = ["blue feather", "yellow feather", "orange feather", "grey feather"]


list_of_numbers.sort()
print(list_of_numbers)

list_of_strings.sort() 
print(list_of_strings)

list_of_numbers.append(3)
list_of_numbers.sort()
print(list_of_numbers)

list_of_numbers.insert(3,10)
print(list_of_numbers)

list_of_numbers.pop(1)
print(list_of_numbers)

list_of_numbers.remove(5)
print(list_of_numbers)


name = "dylan"
print(name.capitalize())

print(name.upper()) #use ".lower" for all lower case

x = input("Do you want to play a game?")
x = x.lower()
if x == "yes":
    print("ok")


lowercase = "small"
if lowercase.islower(): #use "isupper for opposite
    print("yes")
else:
    print("no")
        
guessed = ["w", "a","s","d"]
join_string = "!"
combinded_string = (join_string.join(guessed))
print(combined_string)
