from tabulate import tabulate
from MyException.product_exception import ProductNotFoundException
from Utility.DBconn import DBconnection
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

class ProductService(DBconnection,IProductService):

    def display_product(self):
        try:
           self.cursor.execute("Select * from Product")
           product = self.cursor.fetchall() # Get all data
           headers = [column [0] for column in self.cursor.description]
           print(tabulate (product, headers=headers, tablefmt="psql"))
        except Exception as e:
           print(e)
  
         

    def createProduct(self,name,price,description,stock_quantity):
        try:
           self.cursor.execute( "insert into Product ( name, price, description, stock_quantity) values(?,?,?,?)",
                       (name,price,description,stock_quantity))
           self.conn.commit()
    
        except Exception as e:
           print(e)
      

    def delete_product(self,product_id):
        try: 
            rows_deleted = self.cursor.execute("""
            delete from Order_items where product_id=?
            delete from Cart_items where product_id=?
            delete from Product where product_id=?
            """,
            (product_id,product_id,product_id)
            ).rowcount
            self.conn.commit()
            if rows_deleted == 0:
                    raise ProductNotFoundException(product_id)
            
        except ProductNotFoundException as e:
            print(e)
       