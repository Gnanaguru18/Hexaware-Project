from abc import ABC,abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def display_customer(self):
        pass

    @abstractmethod
    def create_customer(self,customer_name,customer_email,customer_password):
        pass

    @abstractmethod
    def delete_customer(self,customer_id):
        pass
