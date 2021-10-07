
import unittest
from divider import list_divide, ListDivideException


class ListDivideTester(unittest.TestCase):

    def test_list_divide_default(self):
        result = list_divide([1, 2, 3, 4, 5])
        self.assertEqual(result, 2)

        result = list_divide([2, 4, 6, 8, 10])
        self.assertEqual(result, 5)

    def test_list_divide(self):
        result = list_divide([30, 54, 63, 98, 100], divide=10)
        self.assertEqual(result, 2)

    def test_list_divide_empty(self):
        result = list_divide([])
        self.assertEqual(result, 0)

        result = list_divide([], 5)
        self.assertEqual(result, 0)

    def test_list_divide_error(self):
        self.assertRaises(ListDivideException, list_divide, numbers=[30, 54, 63, 98, 100], divide=0)
        self.assertRaises(ListDivideException, list_divide, numbers=[], divide=0)


if __name__ == '__main__':
    unittest.main()
