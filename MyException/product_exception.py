class ProductNotFoundException(Exception):
    def __init__(self, product_id):
       super().__init__(f"Product with ID {product_id} is not found")

