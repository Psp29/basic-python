# insert marks as user input and store it in a list and print them in sorted manner.
m1 = int(input("Please enter marks of student number 1: "))
m2 = int(input("Please enter marks of student number 2: "))
m3 = int(input("Please enter marks of student number 3: "))
m4 = int(input("Please enter marks of student number 4: "))
m5 = int(input("Please enter marks of student number 5: "))
m6 = int(input("Please enter marks of student number 6: "))

# Stores the input values in the list
stuMarkslist = [m1, m2, m3, m4, m5, m6]
stuMarkslist.sort()
print(stuMarkslist)
