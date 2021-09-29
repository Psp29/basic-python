# Encapsulation and Abstraction in OOPS is used to directly access the class and methods without needing to understand where is it coming from or where is it written.
# Also It makes easier for error solving and maintainance of the application in general.

# Encapsulation of Remote press methods
class Remote():
    pass


# Encapsulation of Player movement methods
class Player():
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        pass

    def moveDown(self):
        pass


# Object creation using the class defined
remote1 = Remote()
player1 = Player()

if (remote1.isLeftPressed()):   # Abstraction
    player1.moveLeft()
