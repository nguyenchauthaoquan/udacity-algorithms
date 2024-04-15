from src.trees.nodes import TrieNode


class TrieNode:
    def __init__(self, word=''):
        self.word = word
        self.children = {}
        self.is_word = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for i, char in enumerate(word):
            if char not in current_node.children:
                current_node.children[char] = TrieNode(word=word[:i + 1])
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            else:
                current_node = current_node.children[char]

        return current_node

    def get_suffixes(self, prefix, suffix=''):
        current_node = self.root

        # Traverse the Trie to the end of the prefix
        for char in prefix:
            if char not in current_node.children:
                return []

            current_node = current_node.children[char]

        # Collect suffixes recursively
        suffixes = []
        self._get_suffixes(current_node, suffixes)
        return [suffix + word[len(prefix):] for word in suffixes]

    def _get_suffixes(self, node, suffixes):
        if node.is_word:
            suffixes.append(node.word)

        for child in node.children.values():
            self._get_suffixes(child, suffixes)


if __name__ == '__main__':
    trie_tree = TrieTree()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        trie_tree.insert(word)

    print(trie_tree.find('f').word, trie_tree.find('f').is_word, trie_tree.find('f').children)
    print(trie_tree.get_suffixes(prefix='f'))
