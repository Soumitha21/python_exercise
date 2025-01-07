def trip_cost():
    
    kilometers_to_drive = float(input("Enter the no. of kms to drive: "))
    ltr_per_km = float(input("Enter the car's fuel consumption (liters per kilometer): "))
    price_per_ltr = float(input("Enter the price of fuel per ltr: "))

    
    fuel = kilometers_to_drive * ltr_per_km
    total_cost = fuel * price_per_ltr


    print(f"The cost of the trip is: ${total_cost:.2f}")


trip_cost()




def total_expenses():
    
    quantity = int(input("Enter the quantity of items purchased: "))
    price_per_item = float(input("Enter the price per item: "))

    
    cost1 = quantity * price_per_item

    if quantity > 10:
        discount = cost1 * 0.10
        cost1 -= discount

    
    print(f"The total expenses are: ${cost1:.2f}")

total_expenses()
