class TrieNode:
    def __init__(self, val):
        self.val = val
        self.map = {}
        self.terminal = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(val = None)

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.map:
                curr = curr.map[c]
            else:
                curr.map[c] = TrieNode(val=c)
                curr = curr.map[c]
        curr.terminal = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.map:
                return False
            else:
                curr = curr.map[c]
        return curr.terminal

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.map:
                return False
            else:
                curr = curr.map[c]
        return True