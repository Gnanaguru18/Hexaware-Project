from tabulate import tabulate
from datetime import date
from MyException import CustomerNotFoundException,NoOrdersYetException
from Utility.DBconn import DBconnection
from Interface import IOrderService

class OrderService(DBconnection,IOrderService):

    def Place_order(self, customer_id, shippingAddress):
        try:
            today_date=str(date.today())
            self.cursor.execute("""
            declare @total int= ( select sum( c.quantity * p.price ) from Cart_items c
                                inner join Product p on c.product_id = p.product_id
                                where cart_id = ( select cart_id from Cart
                                                where customer_id= ? ))

            insert into orders (customer_id, order_date, total_price, shipping_address)
            values ( ?, ?, @total, ?)""",
            ( customer_id, customer_id, today_date, shippingAddress)
            )
            self.conn.commit()
            
            self.cursor.execute("""
            select product_id,quantity from Cart_items
            where cart_id = (select cart_id from Cart
							where customer_id = ? )""", customer_id
            ) 
            order = self.cursor.fetchall()
            for i in order:
                self.cursor.execute("""
                insert into Order_items (order_id, product_id, quantity)
                values ((select max(order_id) from orders), ?, ?)""",
                ( i[0], i[1])
                )
                self.cursor.execute("""
                update Product
                set stock_quantity-= ?
                where product_id = ? """,
                ( i[1], i[0])
                )
            self.conn.commit()
            self.cursor.execute("""
            delete from Cart_items
            where cart_id = (select cart_id from Cart where customer_id= ? )""", customer_id
            )
            self.conn.commit()
            print("Order placed successfully........")
            return True

        except Exception as e:
            print(e) 


    def Get_orders_by_customer_alternative(self, customer_id):
        try:
            self.cursor.execute("""
            select oi.product_id,p.name,oi.quantity from orders o inner join
            Order_items oi on o.order_id=oi.order_id inner join
            Product p on p.product_id=oi.product_id
            where o.customer_id= ? """,customer_id
            )
            order = self.cursor.fetchall() 
            if not order:
                raise CustomerNotFoundException(customer_id)
            
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (order, headers=headers, tablefmt="psql"))
        
        except CustomerNotFoundException as e:
            print(e) 
     

    def Get_orders_by_customer(self, customer_id):
        try:
            self.cursor.execute("""
            select order_id from orders
            where customer_id= ?
            """,customer_id
            )
            order = self.cursor.fetchall()
            if len(order)==0:
                raise NoOrdersYetException(customer_id)
            
            order_list = [row[0] for row in order]
            for i in order_list:
                self.cursor.execute("""
                select * from orders
                where customer_id= ? and order_id =?
                """,( customer_id, i)
                )
                sub_order = self.cursor.fetchall() 
                headers = [column [0] for column in self.cursor.description]
                print(tabulate (sub_order, headers=headers, tablefmt="psql"))

        except CustomerNotFoundException as e:
            print(e) 
            
        except NoOrdersYetException as e:
            print(e) 