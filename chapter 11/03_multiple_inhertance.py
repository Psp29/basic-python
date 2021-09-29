class Employee:
    company = "Microsoft"
    eCode = 150


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLvl(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Prasad"


p = Programmer()
p.upgradeLvl()
print(p.company)
print(p.level)
