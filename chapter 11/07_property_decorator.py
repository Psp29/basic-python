class Employee:
    company = "Vincent"
    salary = 50000
    salBonus = 6900
    # totalSal = 5690

    @property
    def totalSal(self):
        return self.salary + self.salBonus

    @totalSal.setter
    def totalSal(self, sal):
        self.salBonus = sal - self.salary


e = Employee()
print(e.totalSal)
e.totalSal = 69000
print(e.salary)
print(e.salBonus)
