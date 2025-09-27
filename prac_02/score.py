"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(score_result(score))

    random_score = 100 * random.random()
    print(f"Random Score: {random_score: .2f}")
    print(score_result(random_score))


def score_result(score: float):
    if 0 <= score <= 100:
        if score >= 90:
            return"Excellent"
        elif score >= 50:
            return"Pass"
        else:
            return"Bad"
    else:
        return"Invalid -  Score [0,100]"


main()