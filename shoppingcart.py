#shopping cart
items = [
    ["Bread", 40],
    ["Cookies", 80],
    ["Cheese", 180],
    ["Butter", 120],
    ["Yoghurt", 60]
]
cart = []

while True:
    print("\nWhat do you want to do")
    print("Press 1 for Viewing the items")
    print("Press 2 for Adding the items")
    print("Press 3 for Updating the items")
    print("Press 4 for Deleting the items")
    print("Press 5 for Billing")
    print("Press 6 to Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Here's our menu:")
        for item in items:
            print(f"Name: {item[0]} Price: {item[1]}")

    elif choice == 2:
        item_name = input("Enter the item name: ").capitalize()
        quantity = int(input("Enter the quantity: "))
        for item in items:
            if item[0] == item_name:
                for cart_item in cart:
                    if cart_item[0] == item_name:
                        cart_item[1] += quantity
                        break
                else:
                    cart.append([item_name, quantity, item[1]])
                break
        else:
            print("Item not available.")

    elif choice == 3:
        item_name = input("What do you want to update: ").capitalize()
        for cart_item in cart:
            if cart_item[0] == item_name:
                updated_quantity = int(input("Enter the updated quantity: "))
                cart_item[1] = updated_quantity
                break
        else:
            print("Item not in cart.")

    elif choice == 4:
        item_name = input("What item do you want to delete: ").capitalize()
        for cart_item in cart:
            if cart_item[0] == item_name:
                cart.remove(cart_item)
                break
        else:
            print("There is no such item in your cart.")

    elif choice == 5:
        print("Billing details:")
        total_amount = 0
        for cart_item in cart:
            item_total = cart_item[1] * cart_item[2]
            total_amount += item_total
            print(f"You ordered {cart_item[0]} in {cart_item[1]} quantity. So the money is: {item_total}")
        print(f"The Total Bill is: {total_amount}")
        print("Thank You, Visit Again")
        break

    else:
        print("Invalid choice. Please try again.")
