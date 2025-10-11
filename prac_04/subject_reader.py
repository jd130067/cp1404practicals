"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_data_from_file(FILENAME)
    for i in range(0, len(subject_data)):
        print(f"{subject_data[i][0]} is taught by {subject_data[i][1]:<12} and has {subject_data[i][2]:>3} students")


def load_data_from_file(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data_points = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_points.append(parts)

    input_file.close()
    return data_points


main()
