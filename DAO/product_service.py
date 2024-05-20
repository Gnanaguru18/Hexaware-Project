from tabulate import tabulate
from MyException.product_exception import ProductNotFoundException
from Utility.DBconn import DBconnection
from Interface import IProductService
class ProductService(DBconnection,IProductService):

    def Display_product(self):
        try:
           self.cursor.execute("Select * from Product")
           product = self.cursor.fetchall() # Get all data
           headers = [column [0] for column in self.cursor.description]
           print(tabulate (product, headers=headers, tablefmt="psql"))
           return product
        except Exception as e:
           print(e)
           return None
  
         

    def Create_product(self,name,price,description,stock_quantity):
        try:
           self.cursor.execute( "insert into Product ( name, price, description, stock_quantity) values(?,?,?,?)",
                       (name,price,description,stock_quantity))
           self.conn.commit()
           print("Product created successfully.........")
           return True
    
        except Exception as e:
           print(e)
      

    def Delete_product(self,product_id):
         
        rows_deleted = self.cursor.execute("""
        delete from Order_items where product_id=?
        delete from Cart_items where product_id=?
        delete from Product where product_id=?
        """,
        (product_id,product_id,product_id)
        ).rowcount
        self.conn.commit()
        try:
            if rows_deleted == 0:
                    raise ProductNotFoundException(product_id)
            
        except ProductNotFoundException as e:
            print(e)
            
        else:
            print(f"Prouct with Product ID:{product_id} has been removed from database.......")
       

    def Check_productid(self,product_id):
        self.cursor.execute("""
        select product_id from Product
        where product_id= ? """,(product_id)
        )
        row=self.cursor.fetchall()
        product_list = [ro[0] for ro in row]
        try:
            if len(product_list)==0:
                raise ProductNotFoundException(product_id)
        except ProductNotFoundException as e:
            print(e)
        finally:
            return len(product_list)
        
    def Get_productId(self,name):
        self.cursor.execute("""
        select product_id from Product
        where name = ? """,name
        )
        product_id=self.cursor.fetchone()[0]
        return product_id