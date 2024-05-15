class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
       super().__init__(f"Customer with ID {customer_id} is not found")