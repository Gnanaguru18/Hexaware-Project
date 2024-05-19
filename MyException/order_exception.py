class OrderNotFoundException(Exception):
    def __init__(self, order_id):
       super().__init__(f"Order with ID {order_id} not found")

class NoOrdersYetException(Exception):
    def __init__(self, customer_id):
        super().__init__(f"No orders placed by customer with customer ID:{customer_id}")