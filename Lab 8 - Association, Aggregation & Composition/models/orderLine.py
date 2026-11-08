from product import Product

class OrderLine(Product):
    def __init__(self, product_id, name, price, stock_quantity, supplier, order_quantity):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.order_quantity = order_quantity
    
    def calculate_subtotal(self) -> float:
        return self.product.price * self.order_quantity