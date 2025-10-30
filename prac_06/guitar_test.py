"""
CP1404 Practical - 06
Testing guitar class
"""

from guitar import Guitar


def main():
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print(f"Gibson age: Expect 103. Got {guitars[0].get_age()}")
    print(f"Gibson vintage: Expect True. Got {guitars[0].is_vintage()}")


if __name__ == "__main__":
    main()
