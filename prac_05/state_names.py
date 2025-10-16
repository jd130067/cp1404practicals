"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

SHORT_TO_LONG_STATE_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                            "WA": "Western Australia",
                            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania",
                            "SA": "South Australia"}

print(SHORT_TO_LONG_STATE_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    if state_code in SHORT_TO_LONG_STATE_NAME:
        print(state_code, "is", SHORT_TO_LONG_STATE_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
