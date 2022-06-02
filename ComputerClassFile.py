class Computer:
    def __init__(self,number_of_cores):
        self.number_of_cores = number_of_cores

    def compute(self):
        print(round(math.pi, self.number_of_cores))

# toaster = Computer(1)
# compy386 = Computer(4)


# toaster.compute()
# compy386.compute()
# output: 3.1
# output: 3.1416