class Employee:
    company = "Microsoft"

    def __init__(self, name, salary, location):
        self.name = name
        self.salary = salary
        self.location = location
        print("\nEmployee is created!!")

    def getDetails(self):
        print(
            f"The name of the Employee is {self.name}.\nSalery is {self.salary}.\nLocation is {self.location}.")

# Taking input from user and printing it
# prasad = Employee(input("Please enter Name of the Employee: "), int(input("Enter salary: ")), input("Enter Location: "))


# Direct giving values into parameters/variables/attributes
prasad = Employee("Prasad", 10000, "Mumbai")

prasad.getDetails()
