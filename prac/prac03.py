
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")

rtan = Person("rtanny")
rtan.sayhello("hanghae")