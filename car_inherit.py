class Vehicle():
    def __init__(self):
        pass

class Electric_Powered():
    def __init__(self):
        pass

class Four_Wheeled():
    def __init__(self):
        pass

class Lightning(Electric_Powered,Four_Wheeled,Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        Electric_Powered.__init__(self)
        Four_Wheeled.__init__(self)

# super().__init__() ??? check Method Resoultuion Order
my_new_rig = Lightning()
help(my_new_rig)

# class Lightning(Vehicle, Electric_Powered, Four_Wheeled)
#  |  Method resolution order:
#  |      Lightning
#  |      Vehicle
#  |      Electric_Powered
#  |      Four_Wheeled
#  |      builtins.object

# moving order of inherited classes changes mtheod resoltuion order
# class Lightning(Electric_Powered, Four_Wheeled, Vehicle)
#  |  Method resolution order:
#  |      Lightning
#  |      Electric_Powered
#  |      Four_Wheeled
#  |      Vehicle
#  |      builtins.object
#  |  