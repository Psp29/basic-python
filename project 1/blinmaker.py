# Blinmaker
# Inspired from 'Life of Boris'

print("Blinmaker is starting up...\n")
flour = int(input("Please Enter amount of flour(mg): "))
milk = int(input("Please Enter amount of milk(ml): "))
egg = int(input("Please Enter amount of egg(s): "))
# Input ends here asking for amount of ingredients.
print()

# Min values required
flourMin = 200
milkMin = 100
eggsMin = 1

# print("You have", flour, "mg of flour!!") # Shows how many amount is entered by user.
# print("You have", milk, "ml of milk!!")
# print("You have", egg, "eggs!!")

# checks if the entered amoun is sufficient or not
if (flour < flourMin or milk < milkMin or egg < eggsMin):
    print("No Blins for today :( ")
else:
    flour = flour / flourMin    # To find the portions of flour
    # print("You have", flour, "portions of flour")
    milk = milk / milkMin   # To find the portions of milk
    # print("You have", milk, "portions of milk")
    # Storing the portion values for easier sorting
    portions = [flour, milk, egg]
    portions.sort()  # Sorting the portion values in ascending order
    print("You can make", (portions[0])*4, "Blin(s) :)")
    print("You will need", (portions[0])*flourMin, "flour.")
    print("You will need", (portions[0])*milkMin, "milk.")
    print("You will need", (portions[0])*eggsMin, "eggs.")

print()
print("Blinmaker Shutting Down...")
