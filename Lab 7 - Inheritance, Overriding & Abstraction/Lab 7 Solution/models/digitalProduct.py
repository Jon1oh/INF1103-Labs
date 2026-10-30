from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, download_size):
        super().__init__(product_id, name, price, stock_quantity) # inherits attributes from parent class
        self.download_size = download_size # an attribute only a digital product has
        
    def display_info(self):
        parent_info = super().__str__()
        return parent_info + f"Download Size: {self.download_size}MB"