stations = [
    "Saddar",
    "Faiz Ahmed Faiz",
    "Potohar",
    "IJP Road",
    "PIMS",
    "Centaurus",
    "Pak Secretariat"
]
buses = [
    {"bus_no": "BRT-101", "departure": "08:00 AM", "seats": 40},
    {"bus_no": "BRT-102", "departure": "09:30 AM", "seats": 35},
    {"bus_no": "BRT-103", "departure": "11:00 AM", "seats": 30}
]

ticket= {}

def welcome ():
    print("=="*30)
    print("Welcome to BRT Islamabad ")
    print("="*30)

## Admin and user Allow  system
def Login_menu():
    print("=====================================")
    print("1. Admin")
    print("2. User")
    print("======================================")

# Admin Login System
def admin():
    
    Admin_name = "Admin"
    Admin_pin = "admin@123"
    correct = False
    
    for i in range (3):
        name = input("Enter Admin Name: ")
        pin = input("Enter PIN: ")

        if name == Admin_name and pin == Admin_pin:
            correct = True
            break
        else:
            print('Wrong PIN Try Again')
        
    if (correct):
        print("Admin Login Sucessfully")
    else:
         print("Account Block some movement")


def admin_Menu():
    print("What Admin Want")
    print("1. Add Station")
    print("2. Add Bus")
    print("3. Exit")
    print()


def add_station():
    print("="*45)
    print("Add Station")
    print()
    name = input("Enter Station Name: ")


    stations.append(name)
    print("Station Add Sucessfully ")


def add_bus():
    print()
    busNo = input("Enter Bus No: ")
    Departure = input("Enter Bus Departure: ")
    seats = int(input("Enter seats Number: "))

    Ad_bus = {
        "bus_no":busNo,
        "departure": Departure,
        "seats":seats
    }

    buses.append(Ad_bus)
    for Ad_bus in buses:

        print("="*45)
        print("Bus No: ",Ad_bus["bus_no"])
        print("Departure: ",Ad_bus["departure"])
        print("seats: ", Ad_bus["seats"])
        print("="*45)

    print(Ad_bus)


def menu():
    print("1. View All Stations")
    print("2. View Available Buses")
    print("4. Check Fare")
    print("3. Search Station")
    print("5. Buy Ticket")
    print("6. View My Ticket")
    print("7. Exit")

    

def view_stations():

    print(f"The Available stations is {stations}")

def view_buses():
    for bus in buses:

        print("Bus No :", bus["bus_no"])
        print("Departure :", bus["departure"])
        print("Seats :", bus["seats"])
        print("-------------------")

def search_station():
    
    print(stations)
    name = input("Enter station name:")
    
    if name in stations:
        print("Station is ",stations)
        print("Station found")

    else: 
        print("Station not found")    

def check_fare():
    print(stations)
    From = input("From: ")
    To = input("To: ")

    if From in stations and To in stations:
        fare = 40
        print("rs", fare)
    else:
        print("invilid Station name")

def buy_ticket():
    global ticket

    name = input("Enter name: ")
    From = input("From: ")
    To = input("To: ")
    fear = 30
    
    ticket ={
        "Name": name,
        "From" : From,
        "To" : To,
        "fear": fear
    }

def view_ticket():

    if ticket == {}:
        print("\nNo ticket found!")
        return

    print("       BRT TICKET")
    print("==========================")
    print("Passenger :", ticket["Name"])
    print("From      :", ticket["From"])
    print("To        :", ticket["To"])
    print("Fare      : Rs.", ticket["fare"])
    
while True:
    welcome()

    Login_menu()
    choice1 = int(input("Enter Your choice: "))
    if choice1 == 1:
        print(":::::::::::::::: Admin Activate ::::::::::::")
        admin()  ## Login System

        admin_Menu()  ## What Admin want to edit
        choice2 = int(input("Admin Choice: "))
        if choice2 == 1:
            add_station()
        elif choice2 == 2:
            add_bus()
        elif choice2 == 3:
            print("Thanks")
            

    else:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_stations()
        elif choice == 2:
            view_buses()
        elif choice == 3:
            search_station()
        elif choice == 4:
            check_fare()
        elif choice == 5:
            buy_ticket()
        elif choice == 6:
            view_ticket()
        elif choice == 7:
            print("\nThank you for using BRT Islamabad. Goodbye!")
            break
        else:
            print("Select Invilid Number ")


