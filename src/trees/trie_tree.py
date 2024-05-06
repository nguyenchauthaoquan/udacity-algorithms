from src.common.constants import ROOT_HANDLER_STR, NOT_FOUND_HANDLER_STR, ROOT_URL_STR, EMPTY_STR
from src.trees.nodes import TrieNode, RouterTrieNode


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


class RouterTrieTree(TrieTree):
    def __init__(self, *handlers):
        super().__init__()
        self.root = RouterTrieNode()
        self.handlers = handlers

    def add_handler(self, handler, paths):
        """
        Add a handler for the pre-defined path
        :param handler: The handler to add path
        :param path: The path to add to the new handler
        """
        current_node = self.root

        for part in paths:
            if part not in current_node.children:
                current_node.children[part] = RouterTrieNode(current_node.path + '/' + part)
            current_node = current_node.children[part]

        if handler in self.handlers:
            current_node.handler = handler
        else:
            self.handlers += (handler,)
            current_node.handler = handler

    def lookup(self, paths):
        """
        lookup path (by path tokens) and return the associated handler
        :param path: The pre-defined path
        :return: The handler of the path
        """
        current_node = self.root

        if paths == ROOT_URL_STR and ROOT_HANDLER_STR in self.handlers:
            return ROOT_HANDLER_STR

        if current_node is None and NOT_FOUND_HANDLER_STR in self.handlers:
            return NOT_FOUND_HANDLER_STR

        for path in paths:
            if path not in current_node.children:
                return NOT_FOUND_HANDLER_STR
            current_node = current_node.children[path]

        return current_node.handler if current_node.handler is not None else NOT_FOUND_HANDLER_STR


if __name__ == '__main__':
    print("Problem 5: ")
    trie_tree = TrieTree()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        trie_tree.insert(word)
    print(trie_tree.get_suffixes(prefix='f'))
