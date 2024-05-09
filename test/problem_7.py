import unittest

from parameterized import parameterized

from src.router.router import Router


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.router = Router("root handler", "not found handler")
        self.router.add_handler("about handler", "/home/about")

    @parameterized.expand([
        ["/", "root handler"],
        ["/home", "not found handler"],
        ["/home/about", "about handler"],
        ["/home/about/", "about handler"],
        ["/home/about/me", 'not found handler'],
        ["", 'not found handler']

    ])
    def test_edge_cases(self, route_lookup, expected_results):
        self.assertEqual(self.router.lookup(route_lookup), expected_results)

    @parameterized.expand([
        ["/", "not found handler"],
        ["/home", "not found handler"],
        ["/home/about", "not found handler"],
        ["/home/about/", "not found handler"],
        ["/home/about/me", 'not found handler'],

    ])
    def test_unhappy_cases_1(self, route_lookup, expected_results):
        self.router = Router()
        self.router.add_handler("", "")
        self.assertEqual(self.router.lookup(route_lookup), expected_results)

    @parameterized.expand([
        ["/"]
    ])
    def test_unhappy_cases_2(self, route_lookup):
        self.router = Router()

        with self.assertRaises(AttributeError):
            self.router.add_handler(None, None)
            self.router.lookup(route_lookup)

    @parameterized.expand([
        ["/", "not found handler"],
        ["/home", "not found handler"],
        ["/home/about", "not found handler"],
        ["/home/about/", "not found handler"],
        ["/home/about/me", 'not found handler']
    ])
    def test_unhappy_cases_3(self, route_lookup, expected_results):
        self.router = Router()
        self.assertEqual(self.router.lookup(route_lookup), expected_results)

    @parameterized.expand([
        [None],
    ])
    def test_unhappy_cases_4(self, route_lookup):
        self.router = Router()
        self.router.add_handler("", "")

        with self.assertRaises(AttributeError):
            self.router.lookup(route_lookup)


if __name__ == '__main__':
    unittest.main()
