#  Create a dictionary program that will take input from user and will give the translation from the dictionary.

hindiDict1 = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Haath": "Hands",
    "Suraj": "Sun"
}

print("Your options are: ", hindiDict1.keys())

a = input("Please Enter the hindi word from the given options above:\n")

print("The meaning of the given word is:", hindiDict1.get(a))
