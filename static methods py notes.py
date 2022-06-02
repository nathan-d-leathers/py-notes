# static methods

class Dog:

    species = "GoodBois"
    all_dogs = []

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        Dog.all_dogs.append(self)

fido = Dog('Fido', 'wolf')

print(fido.species)
# output: GoodBois (instance of class)
print(Dog.species)
# output: GoodBois (class attribute)

roo = Dog("Roo", "Cattle Dog")
rizo = Dog("Chorizo", "XXL Chiwennie")

# for dog in Dog.all_dogs:
#     print(dog.breed)
# output:  
# wolf
# Cattle Dog
# XXL Chiwennie

import math

class Pizza:
    def __init__(self, radius, ingredient):
        self.radius = radius
        self.ingredient = ingredient

    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

mushroom_pizza = Pizza(10, ['mushrooms'])

print(mushroom_pizza.area())
# output:  314.1592653589793

print(Pizza.circle_area(4))
# output:  50.26548245743669


