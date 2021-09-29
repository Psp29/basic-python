class Animals:
    animalType = "Mammal"


class Pets(Animals):
    color = "white"


class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof Woof!")


p = Dog()
print(f"Type: {p.animalType}")
print(f"Color: {p.color}")
print(f"Sound: ", end=""), p.bark()
