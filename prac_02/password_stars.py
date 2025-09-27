"""Checks Minimum Length of Password and Prints Stars"""

MIN_LENGTH = 5

def main():
    password_length = get_password()
    print_asterisks(password_length)


def print_asterisks(password_length: int):
    for i in range(password_length):
        print("*", end="")


def get_password() -> int:
    password = input("Password: ")
    password_length = len(password)

    while password_length < MIN_LENGTH:
        print(f"Minimum Password Length is {MIN_LENGTH}")
        password = input("Password: ")
        password_length = len(password)
    return password_length

main()