from abc import ABC,abstractmethod

class ICartService(ABC):
    @abstractmethod
    def display_cart(self):
        pass

    @abstractmethod
    def add_to_cart(self,customer_id,prod_id,quantity):
        pass

    @abstractmethod
    def remove_from_cart(self,customer_id,prod_id):
        pass

    @abstractmethod
    def getAllFromCart(self,customer_id):
        pass