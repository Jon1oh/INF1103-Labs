from orderLine import OrderLine
from product import Product

class Order:
    def __init__(self, order_id: str, orderLines: list[OrderLine]):
        self.order_id = order_id
        self.order_lines = orderLines
    
    def add_order_line(self, product: Product, order_quantity: int) -> None:
        order_line = OrderLine(product, order_quantity)
        self.order_lines.append(order_line)
        