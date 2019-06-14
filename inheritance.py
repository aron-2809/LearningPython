class Mammal:
    def walk(self):
        print("I'm walking")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def speak(self):
        print("Meow")


Dog().walk()

Cat().speak()