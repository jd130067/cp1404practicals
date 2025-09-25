"""Checks Minimum Length of Password and Prints Stars"""


min_length = 5

password = input("Password: ")
password_length = len(password)

while password_length < 5:
    print(f"Minimum Password Length is {min_length}")
    password = input("Password: ")
    password_length = len(password)

for i in range(password_length):
    print("*", end="")