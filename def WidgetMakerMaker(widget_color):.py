def WidgetMakerMaker(widget_color):

    def WidgetMaker():
        return{
            'type': 'widget',
            'color': widget_color,
        }
    
    return WidgetMaker

RedWidgetMaker = WidgetMakerMaker('red')
red_widget = RedWidgetMaker()

# print(red_widget)


from datetime import datetime

def AddOne(num):
    return num + 1

def MultiplyByTwo(num):
    return num * 2


def PrintCurrentTimeAndAlso(func):
    def WrapperFunction(*args, **kwargs):

        print(f'Calling {func.__name__} at {datetime.now()}')

        return func(*args, **kwargs)
    
    return WrapperFunction

PrintCurrentTimeAndAlsoAddOne = PrintCurrentTimeAndAlso(AddOne)

one_plus_one = PrintCurrentTimeAndAlsoAddOne(1)

print(one_plus_one)
# Output:
# Calling AddOne at 2022-06-01 08:39:54.831589
# 2

PrintCurrentTimeAndAlsoMultiplyByTwo = PrintCurrentTimeAndAlso(MultiplyByTwo)

multiply_by_two = PrintCurrentTimeAndAlsoMultiplyByTwo(2)

print(multiply_by_two)
# output:
# Calling MultiplyByTwo at 2022-06-01 08:43:48.686127
# 4

@PrintCurrentTimeAndAlso
# shorthand to call decorator
def SubtractThree(num):
    return num - 3

nine_subtract_three = SubtractThree(9)
print(nine_subtract_three)
# output:
# Calling SubtractThree at 2022-06-01 08:51:39.915758
# 6

# in generally we will not have to define our own decorators