comment = input("Enter the text: ")

if("make alot of money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("subscribe" in comment):
    spam = True
elif("click on" in comment):
    spam = True
elif("gta6" in comment):
    spam = True
elif("gta 6" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("The comment is a spam comment!")
else:
    print("The comment entered is not a spam :)")
