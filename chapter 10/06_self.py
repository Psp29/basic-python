class Employee:
    company = "Microsoft"

    # Self is an parameter is passed automatically when we call class.
    def getSalary(self):
        print(
            f"Salary of this employee working in {self.company} is Rs.{self.salary}")


prasad = Employee()
prasad.salary = 100000
prasad.getSalary()  # this line read as Employee.getSalary(prasad)
