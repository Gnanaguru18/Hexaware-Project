import unittest

from DAO import ProductService
from Entity.product import Product


class TestProductServiceModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        self.product_service = ProductService()

    def test_add_product(self):
        name='broom'
        price=50
        description='kalimark broom'
        stock_quantity=30
        new_product = Product(name, price, description, stock_quantity)
        created_product = self.product_service.createProduct(new_product)
        self.assertTrue(created_product)


if __name__ == "__main__":
    unittest.main()




# import unittest

# # from ENTITY.Customer import Customer
# from Entity.product import Product
# from DAO import ProductService

# class TestEcommerce(unittest.TestCase):
#     def test_product_creation(self):
#         p = Product(name='Compact Laptop Backpack', price=1999, description= 'Carry your laptop and essentials in style. Designed for comfort, organization, and durability.', stock_quantity=200)
#         result = ProductService.createProduct(p)
#         self.assertEqual(result, True, 'Product Creation Successful.')

#     # def test_customer_registration(self):
#     #     c = Customer(name='Palak Sinha', email = 'palaksinha@email.com', password='palak1234')
#     #     result = ProductService.createCustomer(cob=c)
#     #     self.assertEqual(result, True, 'Customer Registration Successful.')

# if __name__ == '__main__':
#     unittest.main()