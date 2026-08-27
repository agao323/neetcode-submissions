class TrieNode:
    def __init__(self, is_leaf: bool = False):
        self.ref = [None] * 26
        self.is_leaf = is_leaf

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            i = ord(word[i]) - ord('a')
            if not cur.ref[i]:
                cur.ref[i] = TrieNode()                
            cur = cur.ref[i]
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.ref[i]:
                return False
            cur = cur.ref[i]

        return cur.is_leaf

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.ref[i]:
                return False
            cur = cur.ref[i]

        return cur is not None
        