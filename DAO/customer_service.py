from tabulate import tabulate
from Utility.DBconn import DBconnection

class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
       print(f"Customer with ID {customer_id} not found")


class CustomerService(DBconnection):

    def display_customer(self):
        try:
            self.cursor.execute("Select * from Customer")
            cust = self.cursor.fetchall() # Get all data
            headers = [column [0] for column in self.cursor.description]
            print(tabulate (cust, headers=headers, tablefmt="psql"))
        except Exception as e:
            print(e)


    def create_customer(self,customer_name,customer_email,customer_password):
        try:
            self.cursor.execute(
                """INSERT INTO customer (name, email, password) VALUES ( ?, ?, ?)
                declare @a int = (select max(customer_id) from customer)
                insert into cart (customer_id)
                values (@a)   """,
                (customer_name,customer_email,customer_password)
            )
            self.conn.commit()  
        except Exception as e:
            print(e)
  
            

    def delete_customer(self,customer_id):
        rows_deleted = self.cursor.execute(
            """declare @a int = ?;
                    delete from Order_items
                    where order_id= (select order_id
                                    from orders
                                    where customer_id=@a)
                    delete from orders
                    where customer_id=@a

                    delete from Cart_items
                    where cart_id = (select cart_id
                                    from Cart
                                    where customer_id=@a)

                    delete from Cart
                    where customer_id=@a

                    delete from customer
                    where customer_id= @a
            """,
            (customer_id)
        ).rowcount
        self.conn.commit()
        try: 
            if rows_deleted == 0:
                raise CustomerNotFoundException(customer_id)
        except CustomerNotFoundException as e:
            pass


