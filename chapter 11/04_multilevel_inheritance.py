# Parent class
class Person:
    country = "India"
    state = "Maharashtra"

    def getLocation(self):
        print(f"I live in {self.state}, {self.country}.")

# Child class


class HiSchoolStudent(Person):
    college = "Sathaye Jr. College"

    def getStandard(self):
        print("I am currently in 12th standard")

# Child of child class


class UnderGrad(HiSchoolStudent):
    # college = "Harvard"

    def getLocation(self):
        print("I am currently living in USA.")

    def getStandard(self):
        print("I am an Under Graduate student")


p = Person()
p.getLocation()
h = HiSchoolStudent()
u = UnderGrad()
u.getLocation()
print(u.college)
