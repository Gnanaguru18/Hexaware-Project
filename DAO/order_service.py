from tabulate import tabulate
from datetime import date
from Utility.DBconn import DBconnection

class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
       print(f"Customer with ID {customer_id} not found")
class OrderService(DBconnection):

    def placeOrder(self,customer_id, pq_list, shippingAddress):
        try:
            today_date=str(date.today())
            self.cursor.execute(
            """
            insert into orders (customer_id,order_date,shipping_address)
            values (?,?,?)""",
            (customer_id,today_date,shippingAddress)
            
            )
            self.conn.commit()
        
            for i,j in pq_list.items():
                self.cursor.execute("""
                insert into Order_items (order_id,product_id,quantity)
                values ((select max(order_id) from orders), ?,?)""",
                (i,j)
                
                )
                self.conn.commit()

            self.cursor.execute("""
            update orders 
            set total_price=(select sum(price*quantity) from Product
            inner join Order_items on
            Product.product_id=Order_items.product_id 
            where order_id= (select max(order_id) from orders))
            where order_id=(select max(order_id) from orders)
            select * from orders    
                """        
            )
            self.conn.commit()
            print("Your order has been placed")
        except Exception as e:
            print(e)  
       

    def getOrdersByCustomer(self,customer_id):
        try:
            self.cursor.execute(
                """
            select oi.product_id,p.name,oi.quantity from orders o inner join
            Order_items oi on o.order_id=oi.order_id inner join
            Product p on p.product_id=oi.product_id
            where o.customer_id= ? """,
                (customer_id)
            )
            order = self.cursor.fetchall() 
            if not order:
                raise CustomerNotFoundException(customer_id)
            
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (order, headers=headers, tablefmt="psql"))
        
        except CustomerNotFoundException as e:
            pass  
     