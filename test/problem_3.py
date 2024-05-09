import unittest

from parameterized import parameterized

from src.list.list import rearrange_digits


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        [[1, 2, 3, 4, 5], [542, 31]],
        [[4, 6, 2, 5, 9, 8], [964, 852]],
        [[1.1, 2.2, 3.3, 4.4, 5.5], [584.1, 46.2]],
        [[], [0, 0]],

    ])
    def test_edge_cases(self, input_list, expected_results):
        self.assertEqual(sum(rearrange_digits(input_list)), sum(expected_results))

    @parameterized.expand([
        [None]
    ])
    def test_null_case(self, input_list):
        with self.assertRaises(TypeError):
            rearrange_digits(input_list)


if __name__ == '__main__':
    unittest.main()
