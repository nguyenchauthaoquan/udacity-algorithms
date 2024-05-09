import unittest

from parameterized import parameterized

from src.trees.trie_tree import TrieTree


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        words = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]
        self.trie_tree = TrieTree()

        for word in words:
            self.trie_tree.insert(word)


    @parameterized.expand([
        ['a', ['nt', 'nthology', 'ntagonist', 'ntonym']],
        ['an', ['t', 'thology', 'tagonist', 'tonym']],
        ['ant', ['','hology', 'agonist', 'onym']],
        ['f', ['un', 'unction', 'actory']],
        ['fu', ['n', 'nction']],
        ['t', ['rie', 'rigger', 'rigonometry', 'ripod']],
        ['tr', ['ie', 'igger', 'igonometry', 'ipod']],
        ['abcd', []],
    ])
    def test_edge_cases(self, prefix, expected_results):
        self.assertEqual(self.trie_tree.get_suffixes(prefix), expected_results)  # add assertion here


if __name__ == '__main__':
    unittest.main()
