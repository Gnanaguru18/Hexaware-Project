from tabulate import tabulate

class CartService:

    def __init__(self,conn):
        self.conn=conn
        self.cursor=conn.cursor()

   
    def close(self):
        self.cursor.close()
        self.conn.close() 

    def display_cart(self):
        try:
            self.cursor.execute("Select * from Cart_items")
            cart = self.cursor.fetchall() 
            headers = [column [0] for column in cursor.description]
            print(tabulate (cart, headers=headers, tablefmt="psql"))
        except Exception as e:
           print(e)
        finally:
           self.close()
        

    def add_to_cart(self,customer_id,prod_id,quantity):
        try:
            self.cursor.execute(
            """
            declare @a int = (select cart_id from Cart
					    where customer_id= ?);

            insert into Cart_items (cart_id,product_id,quantity)
            values ( @a , ? , ?)
            """,
            (customer_id,prod_id,quantity)
            )
            self.conn.commit()
        except Exception as e:
           print(e)
        finally:
           self.close()

 
    def remove_from_cart(self,customer_id,prod_id):
        try:
            self.cursor.execute(
            """
            declare @a int = (select cart_id from Cart
					where customer_id= ?);

            delete from Cart_items
            where cart_id= @a and product_id = ?
           
            """,
            (customer_id,prod_id)
            )
            self.conn.commit()
        except Exception as e:
           print(e)
        finally:
           self.close()

    def getAllFromCart(self,customer_id):
        try:
            self.cursor.execute(
            """
            select c.customer_id,p.product_id,(p.name) as Product_name,ci.quantity from Cart c inner join
            Cart_items ci on c.cart_id=ci.cart_id
            join Product p on ci.product_id=p.product_id
            where c.customer_id= ?  """,
            (customer_id)
            )
            cart = self.cursor.fetchall() 
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (cart, headers=headers, tablefmt="psql"))
        except Exception as e:
           print(e)
        finally:
           self.close()

       
