class TrieNode:
    def __init__(self, word, prev):
        self.word = word
        self.prev = prev
        self.children = []
