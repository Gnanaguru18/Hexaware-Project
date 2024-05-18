import unittest
import sys
sys.path.append('C:\Local Disk E\Hexaware\Hexaware Project')

from DAO import CustomerService,ProductService
from Entity.customer import Customer


class TestException(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerService()

    def test_customer_id(self):
        customer_id=10002
        customer= self.customer_service.check_customerid(customer_id)
        self.assertIsNotNone(customer)
 


if __name__ == "__main__":
    unittest.main()
