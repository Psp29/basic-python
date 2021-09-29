# (tuples are immutable means that we cannot replace the values in an tuples) and are denoted by brackets i.e. ()
# e.g. x = (3, 'string', 4.0)

# list (it is mutable means they store reference of the items not the copy, basically you can change, append, add, remove items in a list) are denoted by square brackets []
# e.g. x = [4, 'Lassan', 3.5]

x = input("What is your name: ")

if x == 'Boris':
    print('Privyet, ' + x + '!!')

elif x == 'Vadim':
    print(x + ' Blyaat!!')

else:
    print('Hello, ' + x + '!!!')
