from abc import ABC,abstractmethod

class IProductService(ABC):
    
    @abstractmethod
    def Display_product(self):
        pass

    @abstractmethod
    def Create_product(self,name,price,description,stock_quantity):
        pass

    @abstractmethod
    def Delete_product(self,product_id):
        pass
