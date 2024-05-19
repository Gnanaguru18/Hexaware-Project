from tabulate import tabulate
from Utility.DBconn import DBconnection
from Interface import ICartService
from MyException import NoProductInCart,OutOfStockException
class CartService(DBconnection,ICartService):

    def Display_cart(self):
        try:
            self.cursor.execute("Select * from Cart_items")
            cart = self.cursor.fetchall() 
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (cart, headers=headers, tablefmt="psql"))
        except Exception as e:
           print(e)
       

    def Add_to_cart(self,customer_id,prod_id,quantity):
        try:
            self.cursor.execute(
            """
            select stock_quantity from Product
            where product_id=?
            """, prod_id
            )
            stock_quantity=self.cursor.fetchone()[0]

            if stock_quantity-quantity<=-1:
                raise OutOfStockException(prod_id,stock_quantity)

            self.cursor.execute(
            """
            declare @a int = (select cart_id from Cart
					    where customer_id= ?);

            insert into Cart_items (cart_id,product_id,quantity)
            values ( @a , ? , ?)
            """, (customer_id,prod_id,quantity)
            )
            self.conn.commit()
            print(f"Product with product ID {prod_id} has been added to your cart.........")
            return True
        except OutOfStockException as e:
           print(e)
    
 
    def Remove_from_cart(self,customer_id,prod_id):
        try:
            self.cursor.execute(
            """
            declare @a int = (select cart_id from Cart
					where customer_id= ?);

            delete from Cart_items
            where cart_id= @a and product_id = ?
            """, (customer_id,prod_id)
            )
            self.conn.commit()
        except Exception as e:
           print(e)


    def Get_all_from_cart(self,customer_id):
        try:
            self.cursor.execute("""
            select c.customer_id,p.product_id,(p.name) as Product_name,ci.quantity from Cart c inner join
            Cart_items ci on c.cart_id=ci.cart_id
            join Product p on ci.product_id=p.product_id
            where c.customer_id= ?  """,
            (customer_id)
            )
            cart = self.cursor.fetchall() 
            if len(cart)==0:
                raise NoProductInCart(customer_id)
            
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (cart, headers=headers, tablefmt="psql"))
        except NoProductInCart as e:
           print(e)
  
       
