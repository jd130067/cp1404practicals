"""
CP1404 Practical - 06
Testing guitar class
"""

from guitar import Guitar


def main():
    guitars = []
    print("Guitar Collection :)")
    name = input("Name: ")
    while name != "":
        year = get_positive_number("Year")
        cost = get_positive_number("Cost")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    display_guitars(guitars)


def display_guitars(guitars):
    longest_name_length = len(max([guitar.name for guitar in guitars], key=len))
    longest_cost_length = len(max([str(guitar.cost) for guitar in guitars], key=len))

    print(longest_name_length)
    for guitar_index, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {guitar_index+1}: {guitar.name: >{longest_name_length}} ({guitar.year}), worth ${guitar.cost:{longest_cost_length}.2f} {vintage_string} ")


def get_positive_number(input_prompt):
    got_positive_number = False
    while not got_positive_number:
        try:
            result = float(input(f"{input_prompt}: "))
            if result > 0:
                got_positive_number = True
            else:
                print("Invalid Input - Number must be greater than 0")

        except ValueError:
            print("Invalid Input - Please enter a valid number.")
    return result


if __name__ == "__main__":
    main()
