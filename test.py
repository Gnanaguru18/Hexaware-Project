import pyodbc

server_name= "DESKTOP-0EUUQEO\\SQLEXPRESS"
database_name = "Ecom_application"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)
print("Welcome to the movies app")
print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful 🎊")

#####################################################

#product

def read_product():
    cursor.execute("Select * from  Product")
    for i in cursor:
        print(i)


def createProduct(product_id,name,price,description,stock_quantity):
   cursor.execute( "insert into Product values(?,?,?,?,?)",(product_id,name,price,description,stock_quantity))
   conn.commit()

def deleteProduct(product_id):
    cursor.execute("""delete from Order_items where product_id=?
                 delete from Cart_items where product_id=?
                delete from Product where product_id=?""",(product_id,product_id,product_id))
    conn.commit()   

if __name__=="__main__":
   product_id=int(input("enter the product_id: "))
   name=input("Enter the name of the product: ")
   price=int(input("Enter the price: "))  
   description=input("Enter the description: ")
   stock_quantity=int(input("Enter the quantity: "))

createProduct(product_id,name,price,description,stock_quantity)
deleteProduct(product_id)
read_product()

#####################################################33

#customer

