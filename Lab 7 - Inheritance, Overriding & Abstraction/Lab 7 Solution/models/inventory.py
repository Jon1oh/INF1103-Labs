from models.physicalProduct import PhysicalProduct
from models.digitalProduct import DigitalProduct
from tabulate import tabulate
import json, os


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_next_item_id(self):
        if not self.products:
            return 1

        return max(product.get_id() for product in self.products) + 1

    def search_product(self, product_id):
        for product in self.products:
            if product.get_id() == product_id:
                return product

        return None

    def display_inventory(self):
        if not self.products:
            print("\nInventory is empty.\n")
            return

        rows = [
            [
                item.get_id(),
                item.get_name(),
                f"${item.get_price():.2f}",
                item.get_stock_quantity()
            ]
            for item in self.products
        ]

        headers = [
            "Product ID",
            "Product Name",
            "Price",
            "Quantity"
        ]

        print("\nCurrent Inventory")
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        print()

    def update_inventory(self):
        if not self.products:
            print("\nInventory is empty.\n")
            return False

        try:
            product_id = int(input("\nEnter Product ID to update: "))
        except ValueError:
            print("Please enter a valid Product ID.")
            return False

        product = self.search_product(product_id)

        if not product:
            print("Product ID not found.")
            return False

        print(f"\nProduct Name: {product.get_name()}")
        print(f"Current Quantity: {product.get_stock_quantity()}")

        while True:
            try:
                new_quantity = int(input("Enter New Quantity: "))

                if new_quantity < 0:
                    print("Quantity must be 0 or greater.")
                    continue

                product.set_stock_quantity(new_quantity)

                print("\nInventory updated successfully.")
                return True

            except ValueError:
                print("Please enter a valid integer quantity.")

    def save_inventory(self, filename="inventory.json"):
        data = []
        for product in self.products:
            if isinstance(product, PhysicalProduct):
                data.append({
                    "type": "physical",
                    "product_id": product.get_id(),
                    "name": product.get_name(),
                    "price": product.get_price(),
                    "stock_quantity": product.get_stock_quantity(),
                    "weight": product.get_weight # uses @abstractmethod
                })

            elif isinstance(product, DigitalProduct):
                data.append({
                    "type": "digital",
                    "product_id": product.get_id(),
                    "name": product.get_name(),
                    "price": product.get_price(),
                    "stock_quantity": product.get_stock_quantity(),
                    "download_size": product.get_download_size # uses @abstractmethod
                })
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            
    def load_inventory(self, filename="inventory.json"):
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f, indent=4)
            self.products = []
            return

        with open(filename, "r") as f:
            data = json.load(f)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock_quantity"],
                    item["weight"]
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock_quantity"],
                    item["download_size"]
                )

            self.products.append(product)