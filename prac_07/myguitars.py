"""
CP1404 - Practical 07
Program to ...
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
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


if __name__ == "__main__":
    main()
