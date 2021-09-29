# Base/Parent class
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee.")


# Derived/Child class
class Programmer(Employee):  # Inheritance of class Employee.
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}.")

    # If we uncomment te following lines of code then the result of p.getDetails() will be different
    # Basically it overwrites the main class attribute.
    def showDetails(self):
        print("This is an programmer.")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
p.getLang()
