# inheritance is the relationship between two classes when one is a subtype (parent class, child class)
# a dog IS A instance of an animal, if the relationship between two things exsists liek this, inheritance could be useful

# ? what is the __init__ convention called? what other examples are there?
# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def eat(self,food):
#         print(f"{self.name} eats a {food}.") 

#     def meow(self):
#         print('meow meow')

# roo = Cat('roo')
# print(roo)
# roo.eat = 'lasagna'
# print(roo.eat)
# # prints lasanga

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def eat(self,food):
#         print(f"{self.name} eats a {food}.") 

#     def bark(self):
#         print('woof woof')

# roo = Dog('roo')
# print(roo)
# roo.eat = 'hamburger'
# print(roo.eat)
# output: hamburger

# both shared have shared traits. both are instances of being Animals

class Animal:
    def __init__(self,name, color):
        self.name = name
        self.color = color

    def eat(self,food):
        print(f"{self.name} eats a {food}.") 

    def speak(self):
        print('I am an Animal')

class Cat(Animal):
    def speak(self):
        print('meow! meow!')

# garfeild = Cat('garfeild','orange')
# garfeild.eat = 'birthay cake'
# print(garfeild)
# garfeild inherits Animal class and its charecteristics
# print(garfeild.eat)
# # garfeild eats birthday cake
# garfeild.speak()
# output: "meow! meow!", the subclass overrides the parent class

class Dog(Animal):
    def __init__(self,name,color, is_service_animal):
    # need to redefine init for child class if you want to add new attribute to this instance of the parent class
        parent_instance = super()
        # this returns an instance of the animal class (which includes parent class init)
        # alt version below:
        # super().__init__(name)
        parent_instance.__init__(name,color)
        # restate the init method to copy just the self.name attribute from the orignal innit (this is useful for very large classes)
    
        self.is_service_animal = is_service_animal

    def speak(self):
        parent_speech = super().speak()
        # print(parent_speech.upper())
        # some error here with .upper()
        print("but more specifically, ")
        if self.is_service_animal:
            print(f"My name is {self.name} and I am here to help!")
        else:
            print("Bork! Bork!")

rizo = Dog('Rizo','carmel', True)
# eats = rizo.eat('Pepperoni')

# print(rizo)
# output: self statement "Rizo eats a pepperoni"
# print(rizo.color)
# output: carmel
# print(rizo.is_service_animal)
# output: true
# rizo.speak()
# output: Bark! Bark!

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# print(rizo.name)
# print(rizo.color)
# rizo.eat('pepperoni')
# rizo.speak()
# print(rizo.is_service_animal)

# # output below: 

# Rizo
# carmel
# Rizo eats a pepperoni.
# Bark! Bark!
# True
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# add to dog class:

# def speak(self):
#     if self.is_service_animal = True:
#         print(f'My name is {self.name} and I\'m here to help!)
#     else:
#         print(f'{self.speak}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# rizo.speak()
# output after if/else implemented:
# I am an Animal
# but more specifically, 
# My name is Rizo and I am here to help!
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# stick = 'stick'
# print(stick.upper())
# or "stick".upper()
# both output STICK
# not sure why i cant use .upper on parent_speech variable