# main program code/loop here
from inventory_manager import (
    get_new_item_details,
    display_menu, validate_menu_choice,
    confirm_exit_before_saving
    )
from product import Product
from inventory import Inventory

# Main program
print("=" * 40) 
print("INVENTORY MANAGERMENT SYSTEM") # the program banner
print("=" * 40)

inventory = Inventory()
inventory.load_inventory()
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
        inventory.display_inventory()
        
    elif validated_choice == "2": # add product
        new_item = get_new_item_details(inventory) 
        if not new_item: # when user quits during product addition
            continue
            
        product_name, price, quantity = new_item
        new_product = Product(inventory.get_next_item_id(), product_name, price, quantity) # create a new Product object
        inventory.add_product(new_product) # add the new product object to the inventory
        unsaved_changes = True
        print("\nProduct added successfully to the inventory!\n")
        
    elif validated_choice == "3": # update stock
        if inventory.update_inventory(): 
            unsaved_changes = True
    
    elif validated_choice == "4": # search product
        try:
            product_id = int(input("Enter Product ID: "))
            product = inventory.search_product(product_id)
            if product:
                print(product)
            else:
                print("Product ID not found.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif validated_choice == "5":
        inventory.save_inventory() # save inventory
        unsaved_changes = False
        print("Inventory saved successfully.\n")