import unittest
from random import shuffle

from parameterized import parameterized

from src.list.list import find_min_max


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        [[0, 1, 1000, 1000000, 2300000], (0, 2300000), False],
        [[0.5, 20.5, 100.5, 25.5], (0.5, 100.5), False],
        [[], (0, 0), False],
        [[i for i in range(0, 10)], (0, 9), True],
    ])
    def test_edge_cases_1(self, ints, expected_results, is_random):
        if is_random:
            shuffle(ints)
        self.assertEqual(find_min_max(ints), expected_results)

    @parameterized.expand([
        [[0, 1, 1000, 1000000, 2300000], False],
        [[0.5, 20.5, 100.5, 25.5], False],
        [[], False],
        [[i for i in range(0, 10)], True],
    ])
    def test_edge_cases_2(self, ints, is_random):
        if is_random:
            shuffle(ints)

        self.assertEqual(find_min_max(ints), (min(ints) if len(ints) > 0 else 0, max(ints) if len(ints) > 0 else 0))

    @parameterized.expand([
        [None]
    ])
    def test_null_case(self, ints):
        with self.assertRaises(TypeError):
            find_min_max(ints)


if __name__ == '__main__':
    unittest.main()
