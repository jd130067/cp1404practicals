"""
CP1404/CP5632 - Practical
Four tasks for practicing different ways of using files
"""

def main():
    # 1
    input_name = input("Write your name: ")
    write_name_to_file("name.txt", input_name)

    #2
    print_file("name.txt")

    #3
    total = add_numbers_in_file("numbers.txt", 2)
    print(total)
    #4


def write_name_to_file(filename, name):
    out_file_name = open(filename, "w")
    print(name, file=out_file_name)
    out_file_name.close()


def print_file(filename):
    """Prints the entire file contents"""
    in_file_name = open(filename, "r")
    file_contents = in_file_name.read()
    print(file_contents)
    in_file_name.close()

#3
def add_numbers_in_file(filename, number_of_digits_to_add):
    sum_numbers = 0.0
    with open(filename, "r") as in_file:
        for i in range(0, number_of_digits_to_add):
            line = in_file.readline()
            sum_numbers += float(line.strip())

    return sum_numbers


main()
