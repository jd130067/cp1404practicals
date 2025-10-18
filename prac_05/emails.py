"""
Emails
Estimate: 50 minutes
Actual:   .. minutes
Estimate is longer because I forgot how title works and am including time to check.
"""


def main():
    user_email = input("Email: ")
    potential_name = extract_name(user_email)
    print(potential_name)


def extract_name(email):
    username = email.split("@")[0]
    username = username.split(".")
    username = " ".join(username)
    username = username.title()
    return username


main()
