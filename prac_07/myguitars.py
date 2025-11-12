"""
CP1404 - Practical 07
Program to load, change and save a list of guitars using the Guitar class.
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Program to load, change and save a list of guitars."""
    guitars = load_guitars(FILENAME)
    print(f"Loaded {len(guitars)} guitars.")
    name = input("Name: ")
    while name != "":
        year = get_positive_number("Year")
        cost = get_positive_number("Cost")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.sort()
   # print(f"This is guitar list: {guitars}")
    for guitar in guitars:
        print(guitar)
    save_guitars(FILENAME, guitars)


def get_positive_number(input_prompt):
    """Get a positive float from the user."""
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


def load_guitars(filename):
    """Load guitars into a list from a csv."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


def save_guitars(filename, guitars):
    """Save guitars list using class fields into a csv."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            guitar_string = f"{guitar.name},{guitar.year},{guitar.cost}"
            out_file.write(guitar_string + "\n")


if __name__ == "__main__":
    main()
