from tabulate import tabulate
import json, os

def display_menu():    
    print(f"{"-" * 10}MENU{"-" * 10}")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print(f"{"-" * 20}")
    

def validate_menu_choice(choice):
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
        return False
    elif choice == "6":
        return "quit"
    else: # when input is options 1-5
        return choice


def generate_table(headers, rows, title=None, tablefmt="grid"):
    """
    Display a formatted table using tabulate.
    
    Parameters:
        headers (list): Column headings.
        rows (list): List of rows (each row is a list or tuple).
        title (str): Optional table title.
        tablefmt (str): Tabulate format style.
    """
    if title:
        print(f"\n{title}")

    print(tabulate(rows, headers=headers, tablefmt=tablefmt) + "\n")

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)

def load_inventory(filename="inventory.json"):
    # Load inventory from inventory.json. If the file does not exist, return an empty list.
    if not os.path.exists(filename):
        print("\ninventory.json not found. Creating a new inventory file.")
        with open(filename, "w") as f:
            json.dump([], f, indent=4)
        print("Inventory loaded successfully.\n")             
        return []
    with open(filename, "r") as f:
        print("inventory.json found.")
        print("Inventory loaded successfully.\n")
        return json.load(f)

def display_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.\n")
        return

    rows = [
        [
            item["product_id"],
            item["product_name"],
            item["price"],
            item["quantity"]
        ]
        for item in inventory
    ]

    table_headers = ["Product ID", "Product Name", "Price", "Quantity"]
    generate_table(table_headers, rows, "Current Inventory")
        
def update_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.\n")
        return False

    while True:
        product_id_input = input("\nEnter Product ID to update: ").strip()
        if product_id_input == "":
            print("Product ID cannot be empty.")
            continue

        try:
            product_id = int(product_id_input)
            if product_id <= 0:
                print("Product ID must be greater than 0.")
                continue
            break

        except ValueError:
            print("Please enter a valid integer Product ID.")

    for item in inventory:
        if item["product_id"] == product_id:
            print("\nProduct Found")
            print(f"Product Name: {item['product_name']}")
            print(f"Current Quantity: {item['quantity']}")

            while True:
                quantity_input = input("Enter New Quantity: ").strip()
                if quantity_input == "":                    
                    print("Quantity cannot be empty.")
                    continue

                try:
                    new_quantity = int(quantity_input)
                    if new_quantity < 0:
                        print("Quantity must be 0 or greater.")
                        continue
                    
                    item["quantity"] = new_quantity
                    print(f"\nInventory updated successfully.")
                    print(f"New Quantity: {new_quantity}")
                    return True

                except ValueError:
                    print("Please enter a valid integer quantity.")
    print("Product ID not found.")
    return False

def get_next_item_id(inventory):
    if not inventory:
        return 1
    return max(item["product_id"] for item in inventory) + 1

def get_new_item_details():
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
            
def search_item(inventory):
    if not inventory:
        print("\nInventory is empty.\n")
        return False

    product_id_input = input("\nEnter Product ID to search: ").strip()

    if product_id_input == "":
        print("Product ID cannot be empty.")
        return False

    try:
        product_id = int(product_id_input)
    except ValueError:
        print("Please enter a valid integer Product ID.")
        return False

    for item in inventory:
        if item["product_id"] == product_id:

            print("\nProduct Found")
            print("-" * 30)
            print(f"Product ID   : {item['product_id']}")
            print(f"Product Name : {item['product_name']}")
            print(f"Price        : ${item['price']:.2f}")
            print(f"Quantity     : {item['quantity']}")
            print(f"{'-' * 30}\n")
            return True

    print("Product ID not found.")
    return False        
            
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