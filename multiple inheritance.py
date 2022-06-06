from genericpath import samefile
import math
from msilib.schema import Class
from types import ClassMethodDescriptorType

from PersonClass import Person

from ComputerClassFile import Computer

# class Person:
#     def __init__(self,name,job):
#         self.name = name
#         self.job = job

#     def work(self):
#         print(f"{self.name} is working hard as a {self.job}.")


# andy = Person('andy', 'being from kansas')

# andy.work()
# output: andy is working hard as a being from kansas

# class Computer:
#     def __init__(self,number_of_cores):
#         self.number_of_cores = number_of_cores

#     def compute(self):
#         print(round(math.pi, self.number_of_cores))

# toaster = Computer(1)
# compy386 = Computer(4)


# toaster.compute()
# compy386.compute()
# # output: 3.1
# # output: 3.1416

# !!! look up MRO in Python!!!

class MarkZuckerBorg(Person, Computer):
    def __init__(self, name, job, number_of_cores):
        Person.__init__(self,name,job)
        Computer.__init__(self,number_of_cores)
    def work(self):
        for n in range(self.number_of_cores):
            Person.work(self)
zuck = MarkZuckerBorg('Mark', 'hacker', 8)

# zuck.work()
# output:
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.

# !!! Note: module import es6 python devolpers doc for file troublshooting


# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# part 2:

# -commeted out both Person Class and Computer Class
# -put both cl;asses in seperate files 
# -imported both classes.
# -code runs the same

# zuck.work()
# output:
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.
# Mark is working hard as a hacker.


# !!! Note: look up Doom 3 OOP game devleoper .com on werid trick to write better code



# format_map subclass could be useful tool

# str.format_map(mapping)
# Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict. This is useful if for example mapping is a dict subclass:

# >>>
# >>> class Default(dict):
# ...     def __missing__(self, key):
# ...         return key
# ...
# >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
# 'Guido was born in country'
