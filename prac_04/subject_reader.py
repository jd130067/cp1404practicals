"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data_from_file(FILENAME)
    for i in range(0, len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


def load_data_from_file(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data_points = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_points.append(parts)
        # print(parts)  # See if that worked
        # print(data_points)
        # print("----------")

    input_file.close()
    return data_points


main()
