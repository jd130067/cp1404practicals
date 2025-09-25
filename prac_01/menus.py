name = input("Enter name: ")

#!!! Menu Code Format Stolen from temperatures.py

MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f" Hello {name}")
    elif choice == "G":
        print(f" Goodbye {name}")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")