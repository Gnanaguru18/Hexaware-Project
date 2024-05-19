class NoProductInCart(Exception):
    def __init__(self, customer_id):
       super().__init__(f"No item in cart for customer with Customer ID:{customer_id}")