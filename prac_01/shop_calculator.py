"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""
is_valid_input = False
total_price = 0 #My naming was based on the README saying total price not the solutions

#QUESTION FOR FEEDBACK: Should we be doing error checks on everything even if it's not in solutions?

while not is_valid_input:
    try:
        number_of_items = int(input("Number of Items: "))
        if number_of_items < 0:
            print("Invalid number of items!")
            number_of_items = int(input("Number of Items: "))
        else:
            is_valid_input = True

    except ValueError:
        print("Invalid number of items!")

for i in range(0, number_of_items, 1):
    total_price = total_price + float(input("Price of Item: "))

if total_price > 100:
    total_price = total_price - (total_price * 0.1)

print(f"Total price for {number_of_items} items is ${total_price: .2f}")