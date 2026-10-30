from abc import ABC, abstractmethod

class Product(ABC): # ABC makes Product a class template, which can't be used to directly make objects
    def __init__(self, product_id, name, price, stock_quantity, type):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    # display format of product info when an object is created and printed
    def __str__(self):
        return (
            f"Product ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Stock Quantity: {self.stock_quantity}\n"
        )
    
    @abstractmethod # the @abstractmethod makes the method in this class template. Each sub-class must explicitly define what this method does.
    def get_fufilment_info(self):
        pass
        
    # Getters
    def get_id(self):
        return self.product_id
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_stock_quantity(self):
        return self.stock_quantity
        
    # Setters
    def set_id(self, product_id):
        self.product_id = product_id
    
    def set_name(self, name):
        self.name = name
        
    def set_price(self, price):
        self.price = price
        
    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity = stock_quantity