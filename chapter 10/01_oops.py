# Creation of a class to be used afterwards as many times as we want without actually writing extra lines all the times.
class Number():
    def sum(self):
        return self.a + self.b  # Main logic


# Object creation using the class defined
num = Number()
num.a = int(input("Please enter First Number: "))
num.b = int(input("Please enter Second Number: "))
s = num.sum()
print("Sum of entered numbers:", s)

# Procedural way of implementing a program.
# a = 12
# b = 68

# print("The sum of a and b is:", a+b)
