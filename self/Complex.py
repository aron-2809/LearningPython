class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def print(self):
        print(self.r, self.i)


x = Complex(3.0, -4.5)

x.print()