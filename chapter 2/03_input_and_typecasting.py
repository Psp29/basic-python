# input function stores values as 'string' even if value entered is any other datatype.
a = input("Enter a number: ")

# Converts 'a' to an integer (if possible) which is also known as 'typecasting'.
a = int(a)
print(type(a))
