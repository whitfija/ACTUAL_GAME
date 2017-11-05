class MyPet:

    def __init__(self, name):
        self.name = name

    def pet(self):
        print("Your pet ", self.name, " seemed happy to be pet!")

    def make_noise(self):
        print("Noise noise noise.")

orange_cat = MyPet("Miles")
small_dog = MyPet("Fido")

print(orange_cat.name)
small_dog.pet()

class MyDog(MyPet):

    def bark(self):
        print("Woof woof woof.")

my_dog = MyDog("Spike")
my_dog.pet()
my_dog.bark()
