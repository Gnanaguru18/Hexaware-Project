import unittest
import sys
sys.path.append('C:\Local Disk E\Hexaware\Hexaware Project')

from DAO import ProductService
from Entity import Product


class TestProductServiceModule(unittest.TestCase):

    def setUp(self):
        self.product_service = ProductService()

    def test_add_product(self):
        name='Smart Watch'
        price=2000
        description='FireBoltt Amoled'
        stock_quantity=15
        #new_product = Product(name, price, description, stock_quantity)
        created_product = self.product_service.Create_product(name, price, description, stock_quantity)
        self.assertTrue(created_product)

    def test_display_product(self):
        product = self.product_service.Display_product()
        self.assertIsNotNone(product)
        self.assertGreater(len(product), 0)   
    
    def tearDown(self):
        try:
            product_id = self.product_service.Get_productId("Smart Watch")
            self.product_service.Delete_product(product_id)
            print("Teardown Successfull")
        except:
            pass


if __name__ == "__main__":
    unittest.main()
