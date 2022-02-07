"""
Shop calculator
A shop requires a small program that would allow them to quickly
work out total price for a number of items, each with different prices.
The program allows the user to enter the number of items
and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total
before the amount is displayed on the screen.
"""
ItemCount = 0
TotalPrice = 0
Receipt = """
"""
MENU = """I - new Item
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "I":
        quantity = int(input("enter the quantity of the item "))
        while quantity <= 0:
            print("Invalid input. quantity must be greater than 0")
            quantity = int(input("enter the quantity of the item "))
        price = float(input("enter the price of the item "))
        while price <= 0:
            print("Invalid input. price must be greater than 0")
            price = float(input("enter the price of the item "))
        ItemCount = ItemCount + quantity
        TotalItemPrice = quantity * price
        TotalPrice = TotalPrice + TotalItemPrice
        if TotalPrice > 100:
            Discount = TotalPrice / 100 * 10
            TotalPrice = TotalPrice - Discount
        Receipt = Receipt + str(quantity) + """ Items of $ """ + str(price) + """ is $ """ + str(TotalItemPrice) + """
"""

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print(Receipt + """Total price for """ + str(ItemCount) + """ items is $ """ + str(TotalPrice))
