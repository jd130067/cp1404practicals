"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# Value error occurs when input is not an integer
2. When will a ZeroDivisionError occur?
# When denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Can add while loop to force input not to be zero, or just default the input to 1
"""

denominator = 0

try:
    numerator = int(input("Enter the numerator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")