import unittest

from parameterized import parameterized

from src.list.list import sort_012


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        [[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]],
        [[2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]],
        [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]],
        [[]]
    ])
    def test_edge_cases(self, input_list):
        self.assertEqual(sort_012(input_list), sorted(input_list))

    @parameterized.expand([
        [None]
    ])
    def test_null_cases(self, input_list):
        with self.assertRaises(TypeError):
            sort_012(input_list)


if __name__ == '__main__':
    unittest.main()
