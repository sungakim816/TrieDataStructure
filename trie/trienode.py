class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

    def set_children(self, children: dict):
        self.children = children

    def set_is_word(self, is_word: bool):
        self.is_word = is_word
