

# name = input("Enter User Name: ")
# variable name will save what is entered in terminal.
#  example: I enetered "Billiam"
# print("Hello, " + name)
# output:  Hello, Billiam
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# type conversion:

# -int() changes string to number
# -str() changes number to string
# -bool() changes to a True/False statement (look up more info)
# -float() changes to a floating point decimal

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-
# .upper() changes string or variable holding string to uppercase
# .lower() oppsotie of .upper()
# .find() returns first index position of matched charecter or string
# .replace("arg1","arg2") finds and replaces first arg with second arg
# len(variable_name) length of string or list

# sentence = "a single sentence"
# print('single' in sentence)
# output: True (boolean)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-

# equal = 3 == 2
# print(equal) output False (boolean)
# seperating numbers greater than 1000 with _ for readablity(ie: 1_000)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-
# array[0:3] is splice method that returns index 0 through 2 in a new list
# for i in string/list (same as a for loop)
# while loop works the same

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-

# range notes:
# range(5) 
# gives a list of numbers 0-5
# range output generally range(0,5)
# for number in range(5,9):
#     print(number)
# output: 5,6,7,8

# alphabet = range(a,z)
# for char in alphabet:
#     print(char)
# # doesnt work

# can maybe use ord() and chr()

# -ord() function returns the Unicode code from a given character. 
# uni = ord('h')
# print(uni) output: 104
# letta = chr(uni)
# print(letta) output: 'h'
# print(chr(104)) ouput: 'h'

# alphabet = range(ord('a'),ord('z'))
# for char in alphabet:
#     print(chr(char))

# prints full alphabet list of letters
#  output: works!!!

# strang = "strange string"
# print(strang.rsplit())
# output: ['strange', 'string']

# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
# output: banana

# word = 'word'
# splt_word = list(word)
# print(splt_word)
# output: ['w', 'o', 'r', 'd']

# x = lambda a : a + 10
# print(x(5))
# output: 15

# list.sort(reverse=True|False, key=myFunc)


# list.sort(reverse=True) outputs a list in reverse
# list.sort() output a list in ascending order 
# function example:

# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)
# output: sorts list by element length_hint

