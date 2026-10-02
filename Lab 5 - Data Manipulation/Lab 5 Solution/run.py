# main program code/loop here
from persistent_auditor import (
    save_inventory,
    stats,
    load_inventory, display_orders, get_new_order_details, 
    save_summary, save_order, calculate_tax, display_new_order, get_next_order_id, 
    display_menu,
    validate_menu_choice
    )

# Main program
inventory = load_inventory()

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()
    validated_choice = validate_menu_choice(choice)
    
    if validated_choice == "quit": # if valiated_choice is 6
        break
    
    if validated_choice == "1":
        pass # display all products
    elif validated_choice == "2":
        pass # add product
    elif validated_choice == "3":
        pass # update stock
    elif validated_choice == "4":
        pass # search product
    elif validated_choice == "5":
        save_inventory(inventory) # save inventory
        print("Inventory saved successfully.")
    
    # display_orders(orders)
    # result = get_new_order_details() # get quantities for product name and quantity 
    # if result is False:
    #     save_summary(orders)
    #     print(f"\nTotal Failed Validation Attempts: {stats['failed_attempts']}")
    #     print("\nExiting the program.")
    #     break

    # product_name, quantity = result
    # tax = calculate_tax(quantity)
    # new_order = (get_next_order_id(orders), product_name, quantity, tax)

    # save_order(new_order)
    # orders.append(new_order)

    # display_new_order(new_order)
    # print("\nOrder successfully saved to orders.txt\n\n")