from tabulate import tabulate
import json, os

stats = {
    "failed_attempts": 0
}

def display_menu():
    print("=" * 40)
    print("INVENTORY MANAGERMENT SYSTEM")
    print("=" * 40)
    
    print(f"\n{"-" * 10}MENU{"-" * 10}")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print(f"\n{"-" * 20}")
    

def validate_menu_choice(choice):
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        stats["failed_attempts"] += 1
        print("Invalid choice. Please enter a number between 1 and 6.")
        return False
    elif choice == "6":
        print("Thank you for using the Inventory Management System. Goodbye!")
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

    print(tabulate(rows, headers=headers, tablefmt=tablefmt))

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)


def load_inventory(filename="inventory.json"):
    # Load inventory from inventory.json. If the file does not exist, return an empty list.
    if not os.path.exists(filename):
        print("inventory.json not found. Creating a new inventory file.")
        return []
    with open(filename, "r") as f:
        return json.load(f)

def display_orders(orders):
    table_headers = ["Order ID", "Product Name", "Quantity"]
    generate_table(table_headers, orders, "Current Orders")


def get_next_order_id(orders):
    if not orders:
        return 1
    return max(order_id for order_id, _, _, _ in orders) + 1

def get_new_order_details():
    while True:
        product_name = input("\nEnter Product Name (or 'quit' to exit): ").strip()
        
        if product_name.lower() == "quit":
            return False
        if not product_name:
            stats["failed_attempts"] += 1
            print("Product name cannot be empty.")
            continue
        if not product_name.isalpha():
            stats["failed_attempts"] += 1
            print("Product name must contain alphabets only.")
            continue
        break

    while True:
        quantity_input = input("Enter Quantity: ").strip()
        
        if quantity_input == "":
            stats["failed_attempts"] += 1
            print("Quantity cannot be empty.")
            continue

        try:
            quantity = int(quantity_input)

            if quantity < 0:
                stats["failed_attempts"] += 1
                print("Quantity must be 0 or greater.")
                continue

            return product_name, quantity

        except ValueError:
            stats["failed_attempts"] += 1
            print("Invalid input. Please enter a valid integer.")
            
            
# def save_order(order, filename="orders.txt"):
#     """Append a single new order to the file as #order_id,product_name,quantity"""
#     order_id, product_name, quantity = order
#     with open(filename, "a") as f:
#         f.write(f"#{order_id}, {product_name}, {quantity}\n")


# def save_summary(orders, filename="inventory.txt"):
#     with open(filename, "w") as f:
#         f.write(f"Final Total Orders: {len(orders)}\n\n")
#         f.write("Transaction History:\n")

#         for order_id, product_name, quantity in orders:
#             f.write(f"#{order_id}, {product_name}, {quantity}\n")
    
#     print("Inventory summary saved to inventory.txt")


def display_new_order(order):
    table_headers = ["Order ID", "Product Name", "Quantity"]
    generate_table(table_headers, [order], "New Order Added")