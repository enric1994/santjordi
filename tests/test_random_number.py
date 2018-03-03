import unittest
import sys

sys.path.append('../')
import random_number
class TestRandomNumber(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(random_number.generate(-2), -1)
    def test_string(self):
        self.assertEqual(random_number.generate("asd"), -1)
    def test_two_numbers(self):
        self.assertEqual(random_number.generate("1 2"),-1)


if __name__ == '__main__':
    unittest.main()