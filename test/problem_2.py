import unittest

from parameterized import parameterized

from src.list.list import rotated_array_search, linear_search


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6],
        [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1],
        [[6, 7, 8, 1, 2, 3, 4], 8],
        [[6, 7, 8, 1, 2, 3, 4], 1],
    ])
    def test_edge_cases(self, input_list, number):
        self.assertEqual(rotated_array_search(input_list, number), linear_search(input_list, number))

    @parameterized.expand([
        [[6, 7, 8, 1, 2, 3, 4], 10],
        [[], None],
        [[], 4]
    ])
    def test_non_edge_cases(self, input_list, number):
        self.assertEqual(rotated_array_search(input_list, number), linear_search(input_list, number))

    @parameterized.expand([
        [None, None]
    ])
    def test_null_cases(self, input_list, number):
        with self.assertRaises(Exception):
            rotated_array_search(input_list, number)
            linear_search(input_list, number)


if __name__ == '__main__':
    unittest.main()
