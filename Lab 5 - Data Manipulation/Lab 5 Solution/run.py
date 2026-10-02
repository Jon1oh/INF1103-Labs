# main program code/loop here
from inventory_manager import (
    display_inventory, get_next_item_id, save_inventory,
    get_new_item_details, update_inventory,
    load_inventory, save_inventory, display_inventory,
    display_menu, validate_menu_choice,
    confirm_exit_before_saving, search_item
    )

# Main program
print("=" * 40) 
print("INVENTORY MANAGERMENT SYSTEM") # the program banner
print("=" * 40)

inventory = load_inventory()
unsaved_changes = False

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()
    validated_choice = validate_menu_choice(choice)
    
    if validated_choice == "quit": # if valiated_choice is 6
        if confirm_exit_before_saving(unsaved_changes):
            print("Thank you for using the Inventory Management System. Goodbye!")
            break
        else:
            continue
    
    if validated_choice == "1": # display all products
        display_inventory(inventory) 
        
    elif validated_choice == "2": # add product
        new_item = get_new_item_details(inventory) 
        if not new_item: # when user quits during product addition
            continue
            
        product_name, price, quantity = new_item
        new_row = {
            "product_id": get_next_item_id(inventory),
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        inventory.append(new_row) # add the new item to the inventory
        unsaved_changes = True
        print("\nProduct added successfully to the inventory!\n")
        
    elif validated_choice == "3":
        update_inventory(inventory) # update stock
        unsaved_changes = True
    
    elif validated_choice == "4":
        search_item(inventory) # search product
    
    elif validated_choice == "5":
        save_inventory(inventory) # save inventory
        unsaved_changes = False
        print("Inventory saved successfully.\n")
    
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