from abc import ABC,abstractmethod

class IProductService(ABC):
    
    @abstractmethod
    def display_product(self):
        pass

    @abstractmethod
    def createProduct(self,name,price,description,stock_quantity):
        pass

    @abstractmethod
    def delete_product(self,product_id):
        pass
