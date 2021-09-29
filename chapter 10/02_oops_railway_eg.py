class RailwayForm():
    formType = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}.")
        print(f"Train is {self.train}.")


# Object creation using the class defined
myApplication = RailwayForm()
myApplication.name = input("Please Enter your Name: ")
myApplication.train = input("Please Enter Train Name: ")
myApplication.printData()
