from src.common.constants import ROOT_URL_STR, EMPTY_STR
from src.trees.trie_tree import RouterTrieTree


class Router:
    def __init__(self, *handlers):
        self.tree = RouterTrieTree(handlers)

    def add_handler(self, handler, path):
        """
        Add a handler for the pre-defined path
        :param handler: The handler to add path
        :param path: The path to add to the new handler
        """
        paths = self.split_path(path)
        self.tree.add_handler(handler, paths)

    def lookup(self, path):
        """
        lookup path (by path tokens) and return the associated handler
        :param path: The pre-defined path
        :return: The handler of the path
        """
        paths = self.split_path(path)

        return self.tree.lookup(paths)

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
    router = Router("root handler",
                    "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("about handler", "/home/about")  # add a route

    print("Problem 6:")
    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
