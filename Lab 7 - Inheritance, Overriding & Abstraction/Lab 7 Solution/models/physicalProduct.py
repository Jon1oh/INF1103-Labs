from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, weight):
        super().__init__(product_id, name, price, stock_quantity) # inherits attributes from parent class
        self.weight = weight # am attribute that only a physical product has
            
    def display_info(self):
        parent_info = super().__str__()
        return parent_info + f"Weight: {self.weight}"

object = PhysicalProduct(1, "watch", "$5", 10, "0.8kg")
print(object.display_info())