"""
CP1404/CP5632 - Practical
Four tasks for practicing different ways of using files
"""


def main():
    # 1
    out_file = open("name.txt", "w")
    name = input("Write name here: ")
    print(name, file=out_file)
    out_file.close()

    # 2
    in_file = open("name.txt")
    name_from_file = in_file.read().strip()
    in_file.close()
    print(f"Hi, {name_from_file}!")

    # 3
    two_numbers_sum = add_numbers_in_file("numbers.txt", 2)
    print(two_numbers_sum)

    # 4
    lines_to_add = count_lines_in_file("numbers.txt")
    print(add_numbers_in_file("numbers.txt", lines_to_add))


def add_numbers_in_file(filename, number_of_digits_to_add):
    """Sum the numbers on each line of a file."""
    sum_numbers = 0.0
    with open(filename, "r") as in_file:
        for i in range(0, number_of_digits_to_add):
            line = in_file.readline()
            sum_numbers += float(line.strip())

    return sum_numbers


def count_lines_in_file(filename):
    """Count lines in a file."""
    number_of_lines = 0
    with open(filename, 'r') as in_file:
        for line in in_file:
            number_of_lines += 1
    return number_of_lines


main()
