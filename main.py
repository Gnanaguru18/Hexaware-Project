import pyodbc
from datetime import date
from tabulate import tabulate
from DAO import CustomerService,OrderService,CartService,ProductService

class EcomApp:
    def main():
        customer_access=CustomerService()
        cart_access=CartService()
        order_access=OrderService()
        product_access=ProductService()

        while True:
            print("""
                Choose 
                1. Register Customer. 
                2. Create Product. 
                3. Delete Product. 
                4. Add to cart. 
                5. View cart. 
                6. Place order. 
                7. View Customer Order 
                8. Exit""")
            choice=int(input("Enter choice:"))
            if choice==1:
                customer_name=input("Enter Name:")
                customer_email=input("Enter Email:")
                customer_pass=input("Enter Password:")
                customer_access.create_customer(customer_name,customer_email,customer_pass)
                customer_access.display_customer()

            elif choice==2:
                product_name=input("Enter product name:")
                price=int(input("Enter product price:"))
                description=input("Enter product description:")
                stock_quantity=int(input("Enter product quantity:"))
                product_access.createProduct(product_name,price,description,stock_quantity)

            elif choice==3:
                product_access.display_product()
                product_id=int(input("Enter product ID:"))
                product_access.delete_product(product_id)

            elif choice==4:
                product_access.display_product()
                customer_id=int(input("Enter customer ID:"))
                product_id=int(input("Enter product ID:"))
                quantity=int(input("Enter quantity:"))
                cart_access.add_to_cart(customer_id,product_id,quantity)

            elif choice==5:
                customer_id=int(input("Enter customer ID:"))
                cart_access.getAllFromCart(customer_id)

            elif choice==6:
                customer_id=int(input("Enter customer ID:"))
                pq = {}
                num_entries = int(input("Enter the number of products you want to add: "))
                for i in range(num_entries):
                    product = input("Enter product ID: ")
                    quantity = input("Enter quantity: ")
                    pq.update({product: quantity})
                shipping_address=input("Enter shipping address:")
                order_access.placeOrder(customer_id,pq,shipping_address)

            elif choice==7:
                customer_id=int(input("Enter customer ID:"))
                order_access.getOrdersByCustomer(customer_id)

            elif choice==8:
                cart_access.close()
                order_access.close()
                product_access.close()
                customer_access.close()
                print("Thank you for using our service🙏")
                break
            else:
                print("Wrong choice ❌")


if __name__=='__main__':
    app_access=EcomApp
    print("Welcome to Ecom App 🙏")
    app_access.main()
   


