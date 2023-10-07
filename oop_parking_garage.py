class ParkingGarage:
    def __init__(self, capacity):
        self.tickets = list(range(1, capacity + 1))
        self.parkingSpaces = list(range(1, capacity + 1))
        self.currentTicket = {}
        self.capacity = capacity

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.parkingSpaces.remove(ticket)
            self.currentTicket[ticket] = {"paid": False}
            print(f"Ticket {ticket} issued. Please make sure to pay before leaving.")
        else:
            print("Sorry, the garage is full. There are no more tickets available.")

    def payForParking(self):
        ticket = int(input("Please enter your ticket number: "))
        if ticket in self.currentTicket:
            if not self.currentTicket[ticket]["paid"]:
                payment = input("Parking today will be $10. Please enter the payment amount: ")
                if payment == "10":
                    self.currentTicket[ticket]["paid"] = True
                    print(f"Ticket {ticket} has been paid. You have 15 minutes to leave.")
                else:
                    print("Payment cannot be empty.")
            else:
                print("Ticket has already been paid.")
        else:
            print("Invalid ticket number. Please check your ticket.")

    def leaveGarage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]["paid"]:
                self.parkingSpaces.append(ticket)
                self.tickets.append(ticket)
                self.currentTicket.pop(ticket)
                print("Thank you! Have a nice day.")
            else:
                payment = input("Parking today will be $10. Enter the payment amount: ")
                if payment == "10":
                    self.currentTicket[ticket]["paid"] = True
                    self.parkingSpaces.append(ticket)
                    self.tickets.append(ticket)
                    print("Thank you! Have a nice day.")
                else:
                    print("Payment cannot be empty.")
        else:
            print("Invalid ticket number. Please check your ticket.")

    def displayAvailableSpaces(self):
        print(f"Available parking spaces: {len(self.parkingSpaces)}")

def run():
    garage = ParkingGarage(25)  

    while True:
        print("\nPlease select an option:")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave the garage")
        print("4. Display available spaces")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            garage.takeTicket()
        elif choice == "2":
            garage.payForParking()
        elif choice == "3":
            garage.leaveGarage()
        elif choice == "4":
            garage.displayAvailableSpaces()
        elif choice == "5":
            print("Exiting the garage. Goodbye!")
            break
        else:
            print("Please choose one of the available options")

run()