class Employee:
    salary = 2000
    increment = 1.5

    @property
    def salAfterIncrement(self):
        return self.salary*self.increment

    @salAfterIncrement.setter
    def salAfterIncrement(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.salAfterIncrement)

print(e.increment)

# after setter
e.salAfterIncrement = 5000
print(e.increment)
