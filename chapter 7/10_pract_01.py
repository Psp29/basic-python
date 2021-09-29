num = int(input("Enter any number: "))
for i in range(1, 11):
    print(str(num), "X", str(i), "=", str(i*num))
    # print(f"{num}X{i}={num*i}") # we can write above print statement like this using f-string.
