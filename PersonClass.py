class Person:
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def work(self):
        print(f"{self.name} is working hard as a {self.job}.")


# andy = Person('andy', 'being from kansas')

# andy.work()
# output: andy is working hard as a being from kansas