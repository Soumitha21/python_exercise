def display_items(items):
    print("Available items:")
    for item, price in items.items():
        print(f"Name: {item} Price: {price}")

def print_cart(cart):
    print("Current Cart:")
    for item, (quantity, price) in cart.items():
        total = quantity * price
        print(f"{item}, Quantity: {quantity}, Price: {price}, Total: {total}")
    print()

def main():
    items = {
        'Bread': 40,
        'Cookies': 80,
        'Butter': 120,
        'Cheese': 180,
        'Yoghurt': 60
    }

    cart = {}

    while True:
        print("\nWhat do you want to do?")
        print("Enter 1 for viewing the items")
        print("Enter 2 for adding the items in cart")
        print("Enter 3 for updating the items in cart")
        print("Enter 4 for deleting the items in cart")
        print("Enter 5 for printing bill")
        print("Enter 6 to exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_items(items)

        elif choice == 2:
            item_name = input("Enter the item name: ").capitalize()
            if item_name in items:
                quantity = int(input("Enter the quantity: "))
                if item_name in cart:
                    cart[item_name][0] += quantity
                else:
                    cart[item_name] = [quantity, items[item_name]]
            else:
                print("Item not available.")

        elif choice == 3:
            item_name = input("Which item to be updated: ").capitalize()
            if item_name in cart:
                quantity = int(input("Enter the quantity to be updated: "))
                cart[item_name][0] = quantity
            else:
                print("Item not in cart.")

        elif choice == 4:
            item_name = input("Which item to be removed: ").capitalize()
            if item_name in cart:
                del cart[item_name]
            else:
                print("Item not in cart.")

        elif choice == 5:
            print_cart(cart)
            total_amount = sum(quantity * price for quantity, price in cart.values())
            print(f"Total Amount of Bill: {total_amount}")

        elif choice == 6:
            print("Exiting... Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
