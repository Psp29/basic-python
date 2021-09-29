class Employee:
    company = "Google"  # Class Attributes
    salary = 150


prasad = Employee()
piyush = Employee()

# Creation of instance attributes
# prasad.salary = 400
# piyush.salary = 450

print(prasad.company)
print(piyush.company)
print(prasad.salary)
print(piyush.salary)

# Below line will throw an error as 'address' is not present in any class/instance
# print(prasad.address)
