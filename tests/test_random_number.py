import unittest
import sys

<<<<<<< HEAD
sys.path.append('../apps')
=======
sys.path.append('../')
>>>>>>> a86bb1d2b013a17b02d18ebd52f24e5bb4258237
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