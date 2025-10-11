"""
CP1404/CP5632 Practical
Store numbers in a list and output information about them.
"""

whitelisted_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """Tasks 1 and 2 for list exercises."""
    # 1
    numbers = []
    for i in range(5):
        numbers.append(float(input("Number: ")))

    average = sum(numbers)/len(numbers)

    print(f"The first number is {numbers[0]: .1f}")
    print(f"The last number is {numbers[-1]: .1f}")
    print(f"The smallest number is {min(numbers): .1f}")
    print(f"The largest number is {max(numbers): .1f}")
    print(f"The average of the numbers is {average: .1f}")

    # 2
    username = input("Input username for checking: ")
    if username in whitelisted_usernames:
        print("Access granted")
    else:
        print("Access denied")


main()