# Notes taken from Python.org tutorial




# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# M A T H

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-


# print(20 / 4)
# output: 5.0
# division always returns a floating point number

# you can use // to get the nearest whole int
# print(17/3)
# output: 5.666666666666667
# print(17//3)
# output: 5

# ** is used for exponents

# HOW TO GET TWO DECIMAL POINTS:

# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# N O T E: "_" SYMBOL RETURNS LAST PRINTED EXPRESSION
# 113.0625
# >>> round(_, 2)
# 113.06

# j or J is used in python math as an inticator of imainagry number (ie: 3 + 4j)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# S T R I N G S

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# \ escapes an '

# \n will print the follwoing part of a string on a new line
# s = 'First line.\nSecond line.'
# print(s)
# output:
# First line.
# Second line.



# this can also be used in multilines to ommit a single line


# put r befroe string to make it a raw string (no special propeirtes for \)
# >>> print('C:\some\name')  # here \n means newline!
# C:\some
# ame
# >>> print(r'C:\some\name')  # note the r before the quote
# C:\some\name

# sting literals placed next to each other are auto concatinated.

# print('James ' 'Earl ' 'Jones')
# output: James Earl Jones

# can use * to multiple string
# print("Ba- " * 3, "\nBird" * 3, "\nBird is the Word")
# Ba- Ba- Ba-  
# Bird
# Bird
# Bird 
# Bird is the Word

# word = 'python'
# print(word[0:2])
# output: py

# Chart: index of string
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# N O T E: Python strings cannot be changed — they are immutable.

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# STRINGS ARE AN EXAMPLE OF SEQUENCE TYPE AND SUPPORT THOSE OPERATIONS


# S T R I N G - M E T H O D S 


word = 'python'

# print(word.capitalize())
# # output: Python

# print(word.upper())
# output: PYTHON

# print(word.lower())
# output: python


# print(word.endswith('on'))
# # output: true
# same function but reverse: .startswith()


# print(word.count("y"))
# # output: 1

# print(word.center(10,"7"))
# # output: 77python77

# print(word.find("th"))
# # output: 2 (index where "th" begins)
# # alt concept:
# print('py' in 'python')
# # output: True

# print(word.index("h"))
# # output: 3

# print(word.isalnum())
# # output: True (if all charecters are alpha-numeric)

# print(word.isalpha())
# # output: True (if all charecters are alphabetic)

# print(word.isdigit())
# # output: False (if all charecters are numbers)

# other .is() methods
# - .isnumeric() if all chars are digits or unicode
# - .isupper() if all chars are uppercase
# - .islower() if all chars are lowercase
# - .isspace() if includes whitespace
# - .istitle() if in titlecase font

word_two = ['python', 'is', 'rad']

# print(" ".join(word_two))
# # output: 'python is rad'

word_three = " python is kinda fun!"
# print(word_three.title())
# output:  Python Is Kinda Fun!

# print(word.ljust(12,'4'))
# # output: python444444
# also .rjust()

# print(word.removeprefix("py"))
# output: thon
# print(word.removesuffix("on"))
# output: pyth

# N O T E: many methods put an "r" in front of them to indict they work for the opposit direction
# ie: .ljust() works left to right and .rjust() works right to left

# print(word.replace("py","mara"))
# output: marathon

# print(word.split("t"))
# output: ['py', 'hon']
# really only works well on multi word strings
# print(list(word))
# output: ['p','y','t','h','o','n']

# .strip() can remove whitespace or charecters
# print('   spacious   '.strip())
# # output: spacious
# print('www.example.com'.strip('cmowz.'))
# # output: example

# word_four = "How Many TIMES must I TELL YOU!"
# print(word_four.swapcase())
# output: hOW mANY times MUST i tell you!

# print(word.zfill(14))
# output: 00000000python


# to understand further...
# .translate() ???
# .maketrans() ???

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# L I S T S

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# N O T E: Lists are Mutable (can be changed)
list_one = [1,2,3,4,5]

# print(list_one[0])
# # output: 1
# print(list_one[-1])
# # output: 5

list_two = list_one[:]
# print(list_two)
# output: [1, 2, 3, 4, 5]
# N O T E: list_two is a shallow copy of list_one
# using [:] slices the entire list, or makes a copy

list_three = [6,7,8,9,10]
list_four = list_one + list_three
# print(list_four)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lists automatically concatinate
# print(len(list_four))
# output: 10

# can nest like js

# L I S T - M E T H O D S
# n o t e: need to do operations before printing

# list_three.append(11)
# # print(list_three)
# # output: [6, 7, 8, 9, 10, 11]

# list_three.clear()
# # print(list_three)
# # output: []

# print(list_one.count(3))
# output: 1 (returns number of instances)

# list_five = list_four.copy()
# # print(list_five)
# # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list_one.extend(list_four)
# print(list_one)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# r = list_four.index(4)
# print(r)
# output: 3

# list_three.insert(2,'number')
# print(list_three)
# output: [6, 7, 'number', 8, 9, 10]

# list_three.pop()
# print(list_three)
# output: [6, 7, 8, 9] (popped 10)

# list_three.remove(7)
# print(list_three)
# output: [6, 8, 9, 10]

list_seven = ["a","z","k","d","t","e"]
list_seven.reverse()
# print(list_seven)
# output: ['e', 't', 'd', 'k', 'z', 'a']
list_seven.sort()
# print(list_seven)
# output: ['a', 'd', 'e', 'k', 't', 'z']
list_seven.sort(reverse=True)
# print(list_seven)
# output: ['z', 't', 'k', 'e', 'd', 'a']

# n o t e: look into functools
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# T U P P L E S

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
#  n o t e: tupple are immutable lists. 
# you can acess their contents,join two tupples into a new tupple, 
# loop through a tupple, but you cannot change the orginal tupple
# can use range()
# can use len()
my_tupple = (1,3,5,3,7,9)

# T U P P L E - M E T H O D S

# print(my_tupple.count(3))
# output: 2

# print(my_tupple.index(3))
# output: 1 (only returns first instance)

# N O T E !: Tuples cannot be mustated, BUT they can hold mutable items (such as lists)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# S E T S

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

#  n o t e: Sets are used to store multiple item in one variable 

my_set = {"Happy", "Birthday", 2, "You!"}

# can loop
# can add using .add()
# can update using .update (this can add the contacts of one set into another)
set_two = {"And", "Many", "More"}

my_set.update(set_two)
print(my_set)
{2, 'More', 'And', 'Happy', 'Birthday', 'Many', 'You!'}



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# D I C T I O N A R Y S

# TO DO LATER

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-




# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

#  B U I L T - I N  T Y P E S

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# I T E R A T I N G

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# S E Q U E N C E

# There are three basic sequence types: lists, tuples, and range objects.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# useful concepts

combinations = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

squares = square_numbers = [x**2 for x in range(10)]

from math import pi
moving_decimal_points = [str(round(pi, i)) for i in range(1, 6)]
# output: ['3.1', '3.14', '3.142', '3.1416', '3.14159']
matrix = [
[1,2,3,4],
[5,6,7,8],
[9, 10, 11, 12],
]


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

# print(transposed)
# output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed_2 = list(zip(*matrix))
# print(transposed_2)
# output: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

del matrix[0]
# print(matrix)
# output: [5, 6, 7, 8], [9, 10, 11, 12]]

a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
# output: {'r', 'd'}

rando = [4, 9, 9, 5,1,0,45,-5]
# for x in sorted(rando):
#     print(x)

# output:
# -5
# 0
# 1
# 4
# 5
# 9
# 9
# 45

# for x in sorted(set(rando)):
    # print(x)
# output:
# -5
# 0
# 1
# 4
# 5
# 9
# 45

# get key:value pair
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
# output:
# gallahad the pure
# robin the brave

# for i, v in enumerate(['tic', 'tac', 'toe']):
    # print(i,v)
# output:
# 0 tic
# 1 tac
# 2 toe

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))
# output:
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.



# N O T E: sorted(set(iterable)) sorts and filter for duplicates!!!

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# M A T H

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# M A T H

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# M A T H

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-

# M A T H

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
