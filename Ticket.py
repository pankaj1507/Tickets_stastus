class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("***************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in this train is {self.seats}")
        print("***************")


        def getStatus(self):
            print(f"The price of the status is {self.fare}")

        def bookTicket(self):
            if(self.seats>0):
                print(f"your Tickets has been booked! Your seats number is {self.seats}")
                self.seats = self.seats - 1
            else:
                print("Sorry the train is full! kindly try tatkal")

        
intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()