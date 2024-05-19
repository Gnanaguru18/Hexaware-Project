from abc import ABC,abstractmethod

class IOrderService(ABC):

    @abstractmethod
    def Place_order(self,customer_id, shippingAddress):
        pass

    @abstractmethod
    def Get_orders_by_customer(self,customer_id):
        pass
