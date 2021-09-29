a = {7, 8, 9, 10}

# Creating a empty set
b = set()

# Adding new values to an empty set
b.add(1)
b.add(7)
b.add(9)
b.add(5)
b.add(3)
b.add(1)
b.add((1, 3, 5, 7, 9))  # adding a tuple inside a set
print(b)

# Important: We can add hashable datatypes in a set i.e tuples, we cannot add immutable datatypes i.e dictionaries and lists.

print(len(b))   # Returns the length of the set

b.remove(1)  # Removes 1 from the set
print(b)

print(b.pop())  # removes any arbitrary element from the set and returns that element

# print(b.clear())    # Empties the set and returns None
print(b)

print(a.union(b, a))
print(a.intersection(b, a))
