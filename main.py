import time

# Menu & prices
menu = {
    "Big Mac": 3.99,
    "Quarter Pounder": 4.99,
    "McChicken": 3.49,
    "French Fries": 1.49,
    "McFlurry": 2.49,
    "Coca Cola": 1.00,
    "Sprite": 1.00,
    "Fanta": 1.00,
    "Water": 0.99
}

# Order calculator
def calculate_total_price(order):
    total_price = 0
    for item in order:
        total_price += menu[item]
    return total_price

# Delivery
def simulate_delivery():
    print("Your order is being prepared...")
    time.sleep(3)
    print("Your order is on the way!")
    time.sleep(5)
    print("Your order has been delivered. Enjoy your meal!")


def process_input(user_input):
    if "menu" in user_input:
        print("Here's our menu:")
        for item, price in menu.items():
            print(f"{item}: ${price}")
    elif "order" in user_input:
        order = []
        while True:
            item = input("What would you like to order? ")
            if item in menu:
                order.append(item)
                print(f"{item} has been added to your order.")
            else:
                print(f"Sorry, we don't have {item} in our menu.")
            more_items = input("Would you like to order more? (yes/no) ")
            if more_items.lower() == "no":
                break
        total_price = calculate_total_price(order)
        print("Here's your order:")
        for item in order:
            print(item)
        print(f"Total price: ${total_price}")
        delivery_confirmation = input("Would you like us to deliver your order? (yes/no) ")
        if delivery_confirmation.lower() == "yes":
            simulate_delivery()
    elif "track" in user_input or "delivery" in user_input:
        print("Sorry, we don't have a tracking system at the moment.")
    else:
        print("Sorry, I didn't understand that.")

# Start of the program
print("Welcome to McDonald's! For menu type 'menu', To order type 'order'.")
while True:
    user_input = input("> ").lower()
    if user_input == "exit":
        break
    else:
        process_input(user_input)
