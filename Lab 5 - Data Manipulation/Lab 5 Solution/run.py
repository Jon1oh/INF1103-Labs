# main program code/loop here
from persistent_auditor import (
    display_inventory, get_next_item_id, save_inventory,
    stats,
    get_new_item_details, update_inventory,
    load_inventory, save_inventory, display_inventory,
    display_menu, validate_menu_choice
    )

# Main program
print("=" * 40) 
print("INVENTORY MANAGERMENT SYSTEM") # the program banner
print("=" * 40)

inventory = load_inventory()

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()
    validated_choice = validate_menu_choice(choice)
    
    if validated_choice == "quit": # if valiated_choice is 6
        break
    
    if validated_choice == "1": # display all products
        display_inventory(inventory) 
        
    elif validated_choice == "2": # add product
        new_item = get_new_item_details() 
        if not new_item: # when user quits during product addition
            print("\nThank you for using the Inventory Management System.")
            break
        product_name, price, quiantity = new_item
        new_row = [get_next_item_id(inventory), product_name, price, quiantity]
        inventory.append(new_row) # add the new item to the inventory
        print("\nProduct added successfully to the inventory!\n")
        
    elif validated_choice == "3":
        update_inventory(inventory) # update stock
    
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