"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

if 0 <= score <= 100:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Pass")
        else:
            print("Bad")
else:
    print("Invalid -  Score [0,100]")