class TrieNode:
    def __init__(self, word=''):
        self.word = word
        self.children = {}
        self.is_word = False


class RouterTrieNode(TrieNode):
    def __init__(self, path='', handler=None):
        super().__init__()
        self.path = path
        self.handler = handler
