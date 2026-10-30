from product import Product
from interfaces.canBeDownloaded import CanBeDownloaded

class DigitalProduct(Product, CanBeDownloaded):
    def __init__(self, product_id, name, price, stock_quantity, download_size):
        super().__init__(product_id, name, price, stock_quantity) # inherits attributes from parent class
        self.download_size = download_size # an attribute only a digital product has
    
    @property
    def display_info(self):
        parent_info = super().__str__() # inherits the __str__() method from the parent class
        return parent_info + f"Download Size: {self.download_size}MB."
    
    @property
    def get_fufilment_info(self):
        return f"Digital products are downloaded."
    
    @property
    def get_download_size(self):
        return f"The download size is {self.download_size}MB."

file = DigitalProduct(1, "file", "$5", 1, 10)
print(file.display_info)
print(file.get_fufilment_info)
print(file.get_download_size)