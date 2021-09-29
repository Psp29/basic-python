# Rock, Paper and Scissors game.
import random


# createing a function for 'input from player' and computer variable.
def gameWin(p, c):
    if c == p:  # Checks if the values of both player and computer is same or not.
        return None

# Main Game Logic:-
    elif c == 'r':
        if p == 's':
            return False
        elif p == 'p':
            return True

    elif c == 'p':
        if p == 'r':
            return False
        elif p == 's':
            return True

    elif c == 's':
        if p == 'p':
            return False
        elif p == 'r':
            return True
# Main Game Logic ends here.


print("Computer turn: Rock(r), Paper(p) or Scissors(s).")
# random.randint(start,end) will randomly pick one integer from start no. to end no.
randNo = random.randint(1, 3)
if randNo == 1:
    c = 'r'
elif randNo == 2:
    c = 'p'
elif randNo == 3:
    c = 's'

p = input("Player's turn: Rock(r), Paper(p) or Scissors(s)?: ")
a = gameWin(c, p)

print(f"Computer chose {c}")
print(f"You chose {p}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You won!")
else:
    print("You lost!")
