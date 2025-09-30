"""
CP1404/CP5632 - Practical
Four tasks for practicing different ways of using files
"""

def main():
    # 1
    input_name = input("Write your name: ")
    write_name_to_file("name.txt", input_name)

    #2
    read_in_name = read_file("name.txt")
    print(f"Hi, {read_in_name}")

    #3
    two_numbers_sum = add_numbers_in_file("numbers.txt", 2)
    print(two_numbers_sum)

    #4
    lines_to_add = count_lines_in_file("numbers.txt")
    print(add_numbers_in_file("numbers.txt", lines_to_add))


def write_name_to_file(filename, name):
    """Write single line to file."""
    out_file_name = open(filename, "w")
    print(name, file=out_file_name)
    out_file_name.close()


def read_file(filename):
    """Read the entire file contents."""
    in_file_name = open(filename, "r")
    file_contents = in_file_name.read()
    in_file_name.close()
    return file_contents

#3
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
