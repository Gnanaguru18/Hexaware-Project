class ProductNotFoundException(Exception):
    def __init__(self, product_id):
       super().__init__(f"Product with ID {product_id} is not found")

class OutOfStockException(Exception):
    def __init__(self, product_id,quantity):
       super().__init__(f"There are only {quantity} quantity of product with ID {product_id} is available")

