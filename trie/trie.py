from trie.trienode import TrieNode


class Trie:
    def __init__(self):
        self.__root_node = TrieNode()
        self.__suggestion_list = list()

    # add a word to a trie
    def add(self, word: str):
        node = self.__root_node
        for letter in word:
            if letter not in node.children.keys():
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

    # returns a list of suggestion based on the input prefix
    def suggestions(self, word: str) -> list:
        if not self.exists(word):
            return list()
        node = self.__root_node
        self.__suggestion_list.clear()
        for letter in word:  # get the node that has the last letter on the word
            node = node.children[letter]
        self.__suggestions_recursion(word, node)  # recursive deep search
        return self.__suggestion_list

    # recursive deep search
    def __suggestions_recursion(self, word, node: TrieNode):
        if node.is_word:
            self.__suggestion_list.append(word)
        for key in node.children.keys():
            self.__suggestions_recursion(word + key, node.children[key])

    def populate(self, words: list):
        for word in words:
            self.add(word)

    def exists(self, word: str) -> bool:  # method to check if word exist on trie
        if len(word) == 0:
            return False
        node = self.__root_node  # start search on the root node
        for letter in word:
            if letter not in node.children.keys():  # if a letter of a word does not exist, return False
                return False
            node = node.children[letter]  # change node value to one of its child
        return True
