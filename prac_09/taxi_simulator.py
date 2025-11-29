"""
Taxi Simulator Program
Using various taxi classes
- Choose a taxi, how far to drive, then show cost and add up bill.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q) quit, c)hoose taxi, d)rive"


def main():
    """Program to track books and the status of unread or complete"""
    print("Let's drive!")
    print(MENU)

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            if current_taxi:
                drive_taxi(current_taxi)
                bill_to_date += current_taxi.get_fare()
            else:
                print("Please choose a taxi.")
        elif choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_taxi_selection(taxis)
        else:
            print("Invalid Menu Choice.")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total Bill: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """List all taxis and their details."""
    for taxi_index, taxi in enumerate(taxis):
        print(f"{taxi_index} - {taxi}")


def get_taxi_selection(taxis):
    taxi_selection = get_positive_integer("Choose a taxi")
    try:
        current_taxi = taxis[taxi_selection]
        return current_taxi
    except IndexError:
        print("Invalid Taxi Choice")


def get_positive_integer(input_prompt):
    """Get an integer from the user that is above 0."""
    result = -1
    while result < 0:
        try:
            result = int(input(f"{input_prompt}: "))
            if result >= 0:
                return result
            else:
                print("Invalid Input - Integer must be greater than 0")
        except ValueError:
            print("Invalid Input - Please enter a valid integer.")


def drive_taxi(current_taxi):
    """Get distance to drive from user, 'drive' the taxi and display trip cost."""
    distance_to_drive = get_positive_integer("Drive how far?")
    current_taxi.start_fare()
    current_taxi.drive(distance_to_drive)
    print(f"Your {current_taxi.name} trip cost ${current_taxi.get_fare()}")


if __name__ == '__main__':
    main()
