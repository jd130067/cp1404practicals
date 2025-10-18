"""
CP1404/CP5632 Practical
Program to read and display Wimbledon champions and some information about them
"""


def main():
    tennis_champions_data = load_file_data("wimbledon.csv")

    print(tennis_champions_data)


def load_file_data(filename):
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            test = line.strip().split(',')
            champions_data.append(test)
    return champions_data

# set of countries
# dictionary of winners and times won


main()
