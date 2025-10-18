"""
CP1404/CP5632 Practical
Program to read and display Wimbledon champions and some information about them
"""

# TODO fix the naming of champions and things oh my god it's so bad why did i call each row of data champions?

def main():
    tennis_champions_data = load_file_data("wimbledon.csv")
    champions_to_count, countries_set = process_champions_data(tennis_champions_data)
    print(champions_to_count)
    print(countries_set)


def process_champions_data(champion_data):
    """Create dictionary with champion win counts and set of countries that have won."""
    # Counting champions is essentially a copy and paste of word occurrences.
    champion_to_count = {}
    countries_set = set()
    for champion in champion_data:
        try:
            champion_to_count[champion[2]] += 1
        except KeyError:
            champion_to_count[champion[2]] = 1

    for countries in champion_data:
        countries_set.add(countries[1])

    return champion_to_count, countries_set


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
