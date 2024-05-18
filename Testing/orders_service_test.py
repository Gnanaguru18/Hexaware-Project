import unittest
import sys
sys.path.append('C:\Local Disk E\Hexaware\Hexaware Project')


from DAO import OrderService
from Entity.order import Order

class TestProductServiceModule(unittest.TestCase):

    def setUp(self):
        self.order_service = OrderService()

    def test_update_order(self):
        customer_id=10003
        pq_list={20003:3}
        shippingAddress='Leaf village'
        Ordered_product = self.order_service.placeOrder(customer_id, pq_list, shippingAddress)
        self.assertTrue(Ordered_product)


if __name__ == "__main__":
    unittest.main()