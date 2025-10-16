"""
CP1404/CP5632 Practical
Program to lookup hex_codes via colour names.
"""

COLOUR_TO_HEXCODE = {"ALICE BLUE": "#f0f8ff",
                     "APRICOT": "#fbceb1",
                     "AQUA": "#00ffff",
                     "BARN RED": "#7c0a02",
                     "BISTRE": "#3d2b1f",
                     "BLACK": "#000000",
                     "BLACK COFFEE": "#3b2f2f",
                     "BLANCHED ALMOND": "#ffebcd",
                     "CERULEAN": "#1dacd6",
                     "BURGUNDY": "#800020"}

colour_name = input("Enter colour name: ").upper()

while colour_name != "":
    try:
        print(f"{colour_name} has a hexcode of: {COLOUR_TO_HEXCODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()
