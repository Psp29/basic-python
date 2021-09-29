class Employee:
    company = "Google"  # Class Attributes
    salary = 150


prasad = Employee()
piyush = Employee()
# prasad.salary = 400
piyush.salary = 450

print(prasad.company)
print(piyush.company)
Employee.company = "Youtube"
print(prasad.company)
print(piyush.company)
print(prasad.salary)
print(piyush.salary)
