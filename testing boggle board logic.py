# class Oggle:
#     def __init__(self):
#         self.dice = [{123},{456}]
#         self.board = ("""
# new board format
# """)
    
        

# # you can define things that arent part of (self) string

#     def game(self,num):
#         self.num = num
#         if num > 5:
#             print(self.dice)
#         else:
#             print(self.board)

# trie = Oggle()
# trie.game(4)
# # prints new board format
# trie.game(9)
# #  prints dice string

# working!!!
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class Ungle:
#     def __init__(self,char='_'):
#         print('Welcome to the Ungle!')
#         self.char = char
#         for x in range(4):
#             print(f"{char}"*4)


# trunkle = Ungle()
# print(trunkle)

# output:
# Welcome to the Ungle!
# ____
# ____
# ____
# ____

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=
# import random
# class Ungle:
#     def __init__(self,char='_'):
#         print('Welcome to the Ungle!')
#         self.char = char
#         for x in range(4):
#             print(f"{char}"*4)

#     def shake(self):
#         num = 1
#         print(f'Shake {num}')
#         for x in range(4):
#             row = ''
#             for y in range(4):
#                 row += (f"{chr(random.randint(65, 90))}")
#             print(row + '\r')
#             num += 1

# shibo = Ungle()
# shibo.shake()
# output:
# Shake 1
# CKPV
# CLTP
# KIJA
# VMOE

# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import string
import random
class Ungle:
    def __init__(self,char='_'):
        print('Welcome to the Ungle!')
        self.char = char
        for x in range(4):
            print(f"{char}"*4)

    def shake(self):
        num = 1
        charArr = []
        alphabet = (string.ascii_uppercase)
        for char in alphabet:
                charArr.append(char)
        charArr[16] = "Qu"
        print(f'Shake {num}')
        for x in range(4):
            row = ''
            for y in range(4):
              rando = random.randint(0,25)
                row += (f"{charArr[rando]}")
            print(row + '\r')
            num += 1

shibo = Ungle()
shibo.shake()  
# output: Shake 1
# QuXPF
# QuLEN
# GIVQu
# ZXZF