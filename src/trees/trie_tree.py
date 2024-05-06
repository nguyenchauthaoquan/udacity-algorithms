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

    def add_handler(self, handler, path):
        """
        Add a handler for the pre-defined path
        :param handler: The handler to add path
        :param path: The path to add to the new handler
        """
        current_node = self.root
        paths = self.split_path(path)

        for part in paths:
            if part not in current_node.children:
                current_node.children[part] = RouterTrieNode(current_node.path + '/' + part)
            current_node = current_node.children[part]

        if handler in self.handlers:
            current_node.handler = handler
        else:
            self.handlers += (handler,)
            current_node.handler = handler

    def lookup(self, path):
        """
        lookup path (by path tokens) and return the associated handler
        :param path: The pre-defined path
        :return: The handler of the path
        """
        current_node = self.root
        paths = self.split_path(path)

        if path == ROOT_URL_STR and ROOT_HANDLER_STR in self.handlers:
            return ROOT_HANDLER_STR

        if current_node is None:
            return NOT_FOUND_HANDLER_STR

        for path in paths:
            if path not in current_node.children:
                return NOT_FOUND_HANDLER_STR
            current_node = current_node.children[path]

        return current_node.handler if current_node.handler is not None else NOT_FOUND_HANDLER_STR

    def split_path(self, path):
        """
        Split the path into path tokens
        :param path: the pre-defined path
        :return: The list of path tokens
        """
        if path == ROOT_URL_STR:
            return path

        return [part for part in path.split(ROOT_URL_STR) if part != EMPTY_STR]


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

    router = RouterTrieTree("root handler",
                            "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("about handler", "/home/about")  # add a route

    print("Problem 6:")
    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
