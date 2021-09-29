# Base/Parent class
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee.")


# Derived/Child class
class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}.")

    def showDetails(self):
        print("This is an programmer.")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
p.getLang()
