from models.physicalProduct import PhysicalProduct
from models.digitalProduct import DigitalProduct

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

def create_new_product(type, id, name, price, quantity):
    if type == "physical":
        while True:
            try:
                weight = float(input("Enter weight (kg): "))
                if weight < 0:
                    print("Weight must be greater than 0.")
                    continue
                elif not weight:
                    print("Weight can't be empty.")
                    continue
            except ValueError:
                print("Invalid input. Weight must be a float value.")
        
            return PhysicalProduct(id, name, price, quantity, weight)
                    
    if type == "digital":
        while True:
            try:
                download_size = float(input("Enter download size (MB): "))
                if download_size < 0:
                    print("Download size must be greater than 0.")
                    continue
                elif not download_size:
                    print("Download size can't be empty.")
                    continue
            except ValueError:
                print("Invalid input. Download size must be a float value.")
            
            return DigitalProduct(id, name, price, quantity, download_size)
    
        
def get_new_item_details(inventory):
    while True: # Product Type
        print("\nSelect Product Type:\n1. Physical Product\n2. Digital Product")
        product_type = input("Enter choice (1 or 2): ").strip()

        if product_type == "1":
            product_type = "physical"
            break

        elif product_type == "2":
            product_type = "digital"
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    while True: # Product Name
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

    while True: # Product Price
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

    # Product Quantity
    while True:
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
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return product_type, product_name, price, quantity
                        
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