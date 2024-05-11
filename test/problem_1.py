import sys
from random import randint
import unittest

from parameterized import parameterized

import math

from src.math.math import Math


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        [0],
        [0.0],
        [9],
        [16],
        [1],
        [25],
        [9.0]
    ])
    def test_edge_cases(self, number):
        self.assertEqual(Math.sqrt(number), math.sqrt(number))

    @parameterized.expand([
        [9.9],
        [9.5],
        [27],
        [27.5]
    ])
    def test_floating_point_case(self, number):
        self.assertNotEqual(Math.sqrt(number), math.sqrt(number))

    @parameterized.expand([
        [None],
        [''],
    ])
    def test_null_cases(self, number):
        with self.assertRaises(TypeError):
            Math.sqrt(number)


if __name__ == '__main__':
    unittest.main()
