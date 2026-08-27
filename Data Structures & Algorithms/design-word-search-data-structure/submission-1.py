class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        queue = [(self.root, 0)]
        while queue:
            cur, i = queue.pop(0)
            if word[i] == '.':
                for c, child in cur.children.items():
                    if child.end and i == len(word) - 1:
                        return True
                    if i < len(word) - 1:
                        queue.append((child, i + 1))
            else:
                c = word[i]
                if c in cur.children:
                    if i == len(word) - 1 and cur.children[c].end:
                        return True
                    if i < len(word) - 1:
                        queue.append((cur.children[c], i + 1))

        return False
        
