from trie.trie import Trie

words = ['hell', 'apple pie', 'help', 'health', 'hello', 'hello world', 'apple', 'orange', 'heat', 'heal']


def main():
    trie = Trie()
    test_input = 'he'
    trie.populate(words)
    suggestions = trie.suggestions(test_input)

    for word in suggestions:
        print(word)


if __name__ == '__main__':
    main()
