class Train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The available seats in the train are {self.seats}.")

    def getFare(self):
        print(f"Price of a ticket is: Rs.{self.fare}")


pushpak = Train("Pushpak: 69420", 90, 300)
pushpak.getStatus()
pushpak.getFare()
