class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number**0.5}")


a = Calculator(int(input("please enter a number: ")))
a.square()
a.squareRoot()
a.cube()
