from abc import ABC,abstractmethod

class IOrderService(ABC):

    @abstractmethod
    def placeOrder(self,customer_id, pq_list, shippingAddress):
        pass

    @abstractmethod
    def getOrdersByCustomer(self,customer_id):
        pass
