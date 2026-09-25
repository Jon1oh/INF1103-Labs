from tabulate import tabulate

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
                if len(parts) != 3:
                    continue
                order_id_raw, product_name, quantity = parts
                order_id = int(order_id_raw.lstrip("#"))
                orders.append((order_id, product_name, int(quantity)))
    except FileNotFoundError:
        return []
    return orders


def display_orders(orders):
    table_headers = ["Order ID", "Product Name", "Quantity"]
    generate_table(table_headers, orders, "Current Orders")


def get_next_order_id(orders):
    if not orders:
        return 1
    return max(order_id for order_id, _, _ in orders) + 1


def get_new_order_details():
    """Returns (product_name, quantity), or False if the user wants to quit."""
    product_name = input("\nEnter Product Name (or 'quit' to exit): ")
    if product_name.strip().lower() == "quit":
        return False

    while True:
        quantity_input = input("Enter Quantity: ")
        try:
            quantity = int(quantity_input)
            if quantity < 0:
                print("Please try again. Quantity must be 0 or greater.")
                continue
            return product_name, quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def save_order(order, filename="orders.txt"):
    """Append a single new order to the file as #order_id,product_name,quantity"""
    order_id, product_name, quantity = order
    with open(filename, "a") as f:
        f.write(f"#{order_id},{product_name},{quantity}\n")


def save_summary(orders, filename="inventory.txt"):
    with open(filename, "w") as f:
        f.write(f"Final Total Orders: {len(orders)}\n\n")
        f.write("Transaction History:\n")

        for order_id, product_name, quantity in orders:
            f.write(f"#{order_id},{product_name},{quantity}\n")
    
    print("Inventory summary saved to inventory.txt")


def display_new_order(order):
    table_headers = ["Order ID", "Product Name", "Quantity"]
    generate_table(table_headers, [order], "New Order Added")

# Main program
orders = load_inventory()

while True:
    display_orders(orders)
    result = get_new_order_details()
    if result is False:
        save_summary(orders)
        print("\nExiting the program.")
        break

    product_name, quantity = result
    new_order = (get_next_order_id(orders), product_name, quantity)

    save_order(new_order)
    orders.append(new_order)

    display_new_order(new_order)
    print("\nOrder successfully saved to orders.txt\n\n")