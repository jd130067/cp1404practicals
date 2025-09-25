"""Checks Minimum Length of Password and Prints Stars"""


min_length = 5

def main():
    password_length = get_password()

    print_asterisks(password_length)


def print_asterisks(password_length: int):
    for i in range(password_length):
        print("*", end="")


def get_password() -> int:
    password = input("Password: ")
    password_length = len(password)

    while password_length < 5:
        print(f"Minimum Password Length is {min_length}")
        password = input("Password: ")
        password_length = len(password)
    return password_length


main()