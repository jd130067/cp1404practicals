"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
MIN_UPPERCASE = 1
MIN_LOWERCASE = 1
MIN_DIGIT = 1
MIN_SPECIAL_CHARACTER = 1
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += 1
        if character.upper():
            number_of_upper += 1
        if character.isdigit():
            number_of_digit += 1
        if character in SPECIAL_CHARACTERS:
            number_of_special += 1
        pass

    if number_of_lower < MIN_LOWERCASE:
        print(f"Password requires minimum of {MIN_LOWERCASE} lowercase letters")
        return False
    if number_of_upper < MIN_UPPERCASE:
        print(f"Password requires minimum of {MIN_UPPERCASE} uppercase letters")
        return False
    if number_of_digit < MIN_DIGIT:
        print(f"Password requires minimum of {MIN_DIGIT} digits")
        return False
    if (number_of_special < MIN_SPECIAL_CHARACTER) and IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"Password requires minimum of {MIN_SPECIAL_CHARACTER} special characters")
        return False
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()