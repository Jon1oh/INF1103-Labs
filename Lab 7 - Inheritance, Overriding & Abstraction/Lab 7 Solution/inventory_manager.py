def display_menu():    
    print(f"{'-' * 10}MENU{'-' * 10}")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print(f"{'-' * 20}")
    

def validate_menu_choice(choice):
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
        return False
    elif choice == "6":
        return "quit"
    else: # when input is options 1-5
        return choice
    
        
def get_new_item_details(inventory):
    while True: # ask for product name
        product_name = input("\nEnter Product Name (or 'back' to return to main menu): ").strip()

        if product_name.lower() == "back":
            return False

        if not product_name:
            print("Product name cannot be empty.")
            continue

        if not product_name.isalpha():
            print("Product name must contain alphabets only.")
            continue
        
        if any(item.get_name().lower() == product_name.lower() for item in inventory.products): 
            print("Product name already exists in the inventory. Please enter a unique product name.")
            continue
        
        break

    while True: # ask for product price
        price_input = input("Enter Product Price (or 'back' to return to main menu): ").strip()

        if price_input.lower() == "back":
            return False
        
        if price_input == "":
            print("Product price cannot be empty.")
            continue

        try:
            price = float(price_input)
            if price < 0:
                print("Product price must be 0 or greater.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")

    while True: # ask for product quantity
        quantity_input = input("Enter Quantity (or 'back' to return to main menu): ").strip()
        
        if quantity_input.lower() == "back":
            return False
        
        if quantity_input == "":
            print("Quantity cannot be empty.")
            continue
        
        try:
            quantity = int(quantity_input)
            if quantity < 0:
                print("Quantity must be 0 or greater.")
                continue
            return product_name, price, quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")    
            
                        
def confirm_exit_before_saving(unsaved_changes):
    if unsaved_changes:
        while True:
            leave = input("You have unsaved changes. Are you sure you want to exit? All changes will be lost (y/n): ").strip().lower()
            if leave == "y":
                return True
            elif leave == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    else:
        return True