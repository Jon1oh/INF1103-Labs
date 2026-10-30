from product import Product
from interfaces.canBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock_quantity, weight):
        super().__init__(product_id, name, price, stock_quantity) # inherits attributes from parent class
        self.weight = weight # am attribute that only a physical product has

    @property
    def display_info(self):
        parent_info = super().__str__() # inherits the __str__() method from the parent class
        return parent_info + f"Weight: {self.weight}kg"

    @property
    def get_fufilment_info(self):
        return f"Physical produts are shipped."
    
    @property
    def get_shipping_weight(self):
        return f"The shipping weight is {self.weight}kg."
    

object = PhysicalProduct(1, "watch", "$5", 10, 0.8)
print(object.display_info)
print(object.get_fufilment_info)
print(object.get_shipping_weight)