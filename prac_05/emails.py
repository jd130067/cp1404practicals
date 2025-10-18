"""
Emails
Estimate: 50 minutes
Actual:   .. minutes
Estimate is longer because I forgot how title works and am including time to check.
"""


def main():
    user_email = input("Email: ")
    email_to_name = {}
    while user_email != "":
        name = extract_name(user_email)
        choice = input(f"Is your name {name}? [Y/n] ").upper()
        if choice not in ("Y", ""):
            name = input("Please input correct name: ")

        email_to_name[user_email] = name
        print(email_to_name)
        user_email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    username = email.split("@")[0]
    username = username.split(".")
    username = " ".join(username)
    username = username.title()
    return username


main()
