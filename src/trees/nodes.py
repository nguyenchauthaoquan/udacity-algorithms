class TrieNode:
    def __init__(self, word = ''):
        self.word = word
        self.children = {}
        self.is_word = False
