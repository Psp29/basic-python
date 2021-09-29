def game():
    return score


score = input("What is your score? ")

score = game()
with open("highscore.txt") as f:
    highscore = (f.read())

if highscore < score or highscore == 0:
    print("This is new high score!!!\nhighscore.txt is updated successfully...")
    with open("highscore.txt", 'w') as f:
        f.write(str(score))
else:
    print("This is not high score :(\nBetter Luck next time :)")
