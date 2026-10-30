from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, weight):
        super().__init__(product_id, name, price, stock_quantity) # inherits attributes from parent class
        self.weight = weight # a new attribute that the child class will have
        
    def __str__(self):
        return (
            f"Product ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Stock Quantity: {self.stock_quantity}\n"
            f"Weight: {self.weight}"
        )
    
    def display_information(self):
        return self.__str__()