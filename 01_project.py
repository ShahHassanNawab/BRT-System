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
    print("Welcome to BRT Islamabad ")

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
        print("Station found")
    else: 
        print("Station not found")    

def check_fare():
    From = input("From: ")
    To = input("To: ")

    if From in stations and To in stations:
        fare = 30
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
    print("=====================")
    welcome()
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


