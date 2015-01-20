# Trie code from https://github.com/vivekn/autocomplete

# A Trie object, providing autocomplete functionality, intended for 
# providing abbreviated access to collections of strings. It may be
# overkill, as just checking for .startswith might suffice.
class Trie(object):
    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.flag = False    # True indicates that a word ends at this trie node

    def add(self, c):
        val = self.value + c if self.value else c
        self.children[c] = Trie(val)

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.add(c)
            node = node.children[c]
        node.flag = True

    def find(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node.value

    def all_prefixes(self):
        results = set()
        if self.flag:
            results.add(self.value)
        if not self.children:
            return results
        # Below, '|' is the union set operator
        return reduce(lambda a, b: a | b,
                      [node.all_prefixes() for node in self.children.values()]) | results

    def autocomplete(self, prefix):
        node = self
        for c in prefix:
            if c not in node.children:
                return set()
            node = node.children[c]
        return node.all_prefixes()
