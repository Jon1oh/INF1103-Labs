class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    # display format of product info when an object is created and printed
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"
    
    # Getters
    def get_product_id(self):
        return self.product_id
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_stock_quantity(self):
        return self.stock_quantity
    
    # Setters
    def set_product_id(self, product_id):
        self.product_id = product_id
    
    def set_name(self, name):
        self.name = name
        
    def set_price(self, price):
        self.price = price
        
    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity =stock_quantity