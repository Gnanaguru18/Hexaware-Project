from abc import ABC,abstractmethod

class ICartService(ABC):
    @abstractmethod
    def Display_cart(self):
        pass

    @abstractmethod
    def Add_to_cart(self,customer_id,prod_id,quantity):
        pass

    @abstractmethod
    def Remove_from_cart(self,customer_id,prod_id):
        pass

    @abstractmethod
    def Get_all_from_cart(self,customer_id):
        pass