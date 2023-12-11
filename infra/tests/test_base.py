from infra.configs.base import BASE
from sqlalchemy.ext.declarative import declarative_base
import unittest


class TestBase(unittest.TestCase):
    """Must test if BASE is declarative_base()"""

    def setUp(self):
        """Set up the test"""
        self.base = BASE
        return super().setUp()

    def test_base(self):
        """Must test if BASE is declarative_base()"""
        self.assertTrue(isinstance(self.base, declarative_base().__class__))


if __name__ == '__main__':
    unittest.main()
