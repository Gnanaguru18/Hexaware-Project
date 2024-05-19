from abc import ABC,abstractmethod

class IOrderService(ABC):

    @abstractmethod
    def place_order(self,customer_id, pq_list, shippingAddress):
        pass

    @abstractmethod
    def get_orders_by_customer(self,customer_id):
        pass
