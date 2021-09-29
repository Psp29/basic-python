class Employee:
    company = "Amigas"
    salary = "69420"
    location = "Deathvally"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod    # we can change or add the class attribute itself without creating new instance attribute
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(60)
print(e.salary)
print(Employee.salary)
