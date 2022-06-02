# Pthyon OOP Notes:

from turtle import color


class Dog:
    # pass
    # pass is a python statement that does nothing
    # dunder-init (double Underscores)
    def __init__(self, name, color,vaccination_status, sound="woof"):
        #  if you want to include the fn, ln inlucde it in innit string
        # fn = first_name
        # ln = last_name
        # self.name = fn + " " + ln
        self.name = name
        self.species = "dog"
        self.color = color
        self.sound = sound
        self.vaccination_status = vaccination_status
        self.barks = 0
    def __str__(self):
        return f"I am a {self.color} {self.species} named {self.name}"
    
    def speak(self):
        self.barks += 1
        print(f"{self.name} says {self.sound}!")
    
    def yell(self):
        return self.speak()
        # having problems using .speak().upper()

    def fetch(self,item):
        print(f"{self.name} fetched the {item}.")
    


rizo = Dog('Chorizo', "carmel", "up to date", 'hoooowl')
# rizo is an INSTANCE of a Class
# rizo.color = "brown",   output reasigns color 
# rizo.toy = "ball",  output adds new atrribute to instance
# excited_greeting = str(rizo) + "!!!", outputs class string concated with "!!!" string
# print(excited_greeting) I am a Dog named Fido.!!!
# print(fido) I am a Dog named Fido
# print(rizo.vaccination_status)
# print(rizo.speak())
# rizo.fetch('bones'),  output: Chorizo fetched the bones.
# rizo.speak()
# print(rizo.yell()) problem calling this mehid

class Person:
    def __init__(self,name,dog_name):
        self.name = name
        self.dog = Dog(dog_name, 'black', 'bark')


nathan = Person('nathan', 'roo')
# print(nathan)  prints type of obj 
print(nathan.dog) 
# output: I am a black dog named roo

