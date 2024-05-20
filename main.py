from DAO import CustomerService,OrderService,CartService,ProductService

class EcomApp:
    def main():
        customer_access=CustomerService()
        cart_access=CartService()
        order_access=OrderService()
        product_access=ProductService()

        while True:
            print("""
                Main Menu 
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
                customer_access.Create_customer(customer_name,customer_email,customer_pass)
                

            elif choice==2:
                product_name=input("Enter product name:")
                price=int(input("Enter product price:"))
                description=input("Enter product description:")
                stock_quantity=int(input("Enter product quantity:"))
                product_access.Create_product(product_name,price,description,stock_quantity)
                

            elif choice==3:
                product_access.Display_product()
                product_id=int(input("Enter product ID:"))
                product_access.Delete_product(product_id)

            elif choice==4:
                product_access.Display_product()
                customer_id=int(input("Enter customer ID:"))
                if customer_access.Check_customerid(customer_id)==0:
                    continue
                product_id=int(input("Enter product ID:"))
                if product_access.Check_productid(product_id)==0:
                    continue
                quantity=int(input("Enter quantity:"))
                cart_access.Add_to_cart(customer_id,product_id,quantity)

            elif choice==5:
                customer_id=int(input("Enter customer ID:"))
                if customer_access.Check_customerid(customer_id)==0:
                    continue
                cart_access.Get_all_from_cart(customer_id)

            elif choice==6:
                customer_id=int(input("Enter customer ID:"))
                if customer_access.Check_customerid(customer_id)==0:
                    continue
                shipping_address=input("Enter shipping address:")
                order_access.Place_order(customer_id,shipping_address)

            elif choice==7:
                customer_id=int(input("Enter customer ID:"))
                if customer_access.Check_customerid(customer_id)==0:
                    continue
                order_access.Get_orders_by_customer(customer_id)

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
   


