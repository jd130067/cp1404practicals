import random

NUMBERS_PER_PICK = 6
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45


def main():
    """Program to create as many quick picks as needed."""
    number_of_picks = int(input("How many quick picks?: "))
    quick_picks = generate_quick_picks(number_of_picks)
    for i in quick_picks:
        print(" ".join(f"{number_in_pick:2}" for number_in_pick in i)) # I'm quite proud of this


def generate_quick_picks(number_of_picks):
    """Generates nested lists of sorted quick picks."""
    collated_quick_picks = []
    for i in range(number_of_picks):
        current_quick_pick = []
        while len(current_quick_pick) < NUMBERS_PER_PICK:
            random_number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
            if not(random_number in current_quick_pick):
                current_quick_pick.append(random_number)

        current_quick_pick.sort()

        collated_quick_picks.append(current_quick_pick)
    return collated_quick_picks


main()
