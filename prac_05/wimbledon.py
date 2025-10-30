"""
CP1404/CP5632 Practical
Program to read and display Wimbledon champions and some information about them
"""

FILENAME = "wimbledon.csv"


def main():
    """Program to load Wimbledon data, process it and display it"""
    mens_singles_wimbledon_history = load_file_data(FILENAME)
    champions_to_count, countries_set = process_champions_data(mens_singles_wimbledon_history)
    display_information(champions_to_count, countries_set)


def display_information(champions_to_count, countries_set):
    """Display champions, how many times they've won and countries that have won"""
    print("Wimbledon Champs:")
    longest_name = len(max(champions_to_count, key=len))
    for champion, count in champions_to_count.items():
        print(f"{champion:{longest_name}} won {count} times")
    print()
    print("These countries have won Wimbledon:")
    country_list = ", ".join(countries_set)
    print(country_list)


def process_champions_data(wimbledon_data_record):
    """Create dictionary with champion win counts and set of countries that have won."""
    # Counting champions is essentially a copy and paste of word occurrences.
    champion_to_count = {}
    countries_set = set()
    for row_in_record in wimbledon_data_record:
        countries_set.add(row_in_record[1])
        try:
            champion_to_count[row_in_record[2]] += 1
        except KeyError:
            champion_to_count[row_in_record[2]] = 1

    return champion_to_count, countries_set


def load_file_data(filename):
    """Create nested lists using file data."""
    file_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            test = line.strip().split(',')
            file_data.append(test)
    return file_data


main()
