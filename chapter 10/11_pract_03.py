class Sample:
    a = "Prasad"    # Class attribute


obj = Sample()
obj.a = "Piyush"    # Instance Attribute
# Sample.a = "Piyush" # It will change the class attribute

print(Sample.a)  # It will print Prasad
print(obj.a)    # It will print Piyush
# Above lines will not retrive same values because one of them is a class attribute and other is an instance attribute they behave differently eventhough the variable(a) is same.
