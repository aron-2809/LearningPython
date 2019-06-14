class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi i am {self.name}")


john = Person("John Smith")
print(john.name)
print(john.talk())

bob = Person("Bob Marley")
print(bob.name)
print(bob.talk())