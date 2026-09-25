from tabulate import tabulate

stats = {
    "failed_attempts": 0
}

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


def calculate_tax(quantity):
    tax = 0.1 * quantity
    formatted_tax = f"${tax:.2f}"
    return formatted_tax


def load_inventory(filename="orders.txt"):
    """Read existing orders from file. Returns a list of
    (order_id, product_name, quantity) tuples. If the file doesn't
    exist, returns an empty list so the program can start fresh."""
    orders = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 4:
                    continue
                order_id_raw, product_name, quantity, tax = parts
                order_id = int(order_id_raw.lstrip("#"))
                orders.append((order_id, product_name, int(quantity), tax))
    except FileNotFoundError:
        return []
    return orders


def display_orders(orders):
    table_headers = ["Order ID", "Product Name", "Quantity", "Tax"]
    generate_table(table_headers, orders, "Current Orders")


def get_next_order_id(orders):
    if not orders:
        return 1
    return max(order_id for order_id, _, _, _ in orders) + 1


def get_new_order_details():
    """
    Returns (product_name, quantity),
    or False if the user wants to quit.
    """

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
            
            
def save_order(order, filename="orders.txt"):
    """Append a single new order to the file as #order_id,product_name,quantity"""
    order_id, product_name, quantity, tax = order
    with open(filename, "a") as f:
        f.write(f"#{order_id}, {product_name}, {quantity}, {tax}\n")


def save_summary(orders, filename="inventory.txt"):
    with open(filename, "w") as f:
        f.write(f"Final Total Orders: {len(orders)}\n\n")
        f.write("Transaction History:\n")

        for order_id, product_name, quantity, tax in orders:
            f.write(f"#{order_id}, {product_name}, {quantity}, {tax}\n")
    
    print("Inventory summary saved to inventory.txt")


def display_new_order(order):
    table_headers = ["Order ID", "Product Name", "Quantity", "Tax"]
    generate_table(table_headers, [order], "New Order Added")

# Main program
orders = load_inventory()

while True:
    display_orders(orders)
    result = get_new_order_details() # get quantities for product name and quantity 
    if result is False:
        save_summary(orders)
        print(f"\nTotal Failed Validation Attempts: {stats["failed_attempts"]}")
        print("\nExiting the program.")
        break

    product_name, quantity = result
    tax = calculate_tax(quantity)
    new_order = (get_next_order_id(orders), product_name, quantity, tax)

    save_order(new_order)
    orders.append(new_order)

    display_new_order(new_order)
    print("\nOrder successfully saved to orders.txt\n\n")