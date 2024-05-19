from abc import ABC,abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def Display_customer(self):
        pass

    @abstractmethod
    def Create_customer(self,customer_name,customer_email,customer_password):
        pass

    @abstractmethod
    def Delete_customer(self,customer_id):
        pass
