"""Score Menu: Get Valid Score, Print Result, Prints as Many Stars as Score, Quit"""

import math

def main():
    score = get_valid_score()
    menu = """G - Press "G" to input your score
    P - Press "P" to see your result
    S - Pretty Stars :)
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            score_result_readable = score_result(score)
            print(score_result_readable)
        elif choice == "S":
            integer_score = int(math.ceil(score)) #rounding up cuz more stars better
            print_asterisks(integer_score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("I guess this is goodbye :(")


def score_result(score: float):
    """Categorise float into excellent, pass or bad."""
    #Score Validity Check Done in Separate Function
    if score >= 90:
        return"Excellent"
    elif score >= 50:
        return"Pass"
    else:
        return"Bad"


def print_asterisks(number_of_stars: int):
    """Print an integer number of stars."""
    for i in range(number_of_stars):
        print("*", end="")

    print()


def get_valid_score():
    """Get a float input from user between 0 and 100."""
    is_score_valid = False
    while not is_score_valid:
        score = float(input("Input Score (0-100): "))
        if 0 <= score <= 100:
            is_score_valid = True
            return score
        else:
            print("Your score needs to be from 0 - 100")

    return None

main()