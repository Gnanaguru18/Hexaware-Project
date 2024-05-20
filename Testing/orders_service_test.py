import unittest
import sys
sys.path.append('C:\Local Disk E\Hexaware\Hexaware Project')


from DAO import OrderService
from Entity import Order

class TestProductServiceModule(unittest.TestCase):

    def setUp(self):
        self.order_service = OrderService()

    def test_update_order(self):
        customer_id=10003
        shippingAddress='Leaf village'
        Ordered_product = self.order_service.Place_order(customer_id,shippingAddress)
        self.assertTrue(Ordered_product)


if __name__ == "__main__":
    unittest.main()