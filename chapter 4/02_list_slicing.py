# List slicing
a = [1, 3, 4, 23, 343, 66, 69]
print(a[1:5])   # It will print the elements from 1st index to 4th
print(a[:6])    # Same as a[0:6]
print(a[5:])    # will print from 5th pos to last
# Here, first 0 is first element, second 0 is last item and last 2 is the gap
print(a[::2])
print(a[-4::2])
