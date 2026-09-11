class Node:
    
    def __init__(self, value):
        self.value = value
        self.hashmap = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = Node(value = None)

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.hashmap:
                curr = curr.hashmap[c]
            else:
                new_node = Node(value = c)
                curr.hashmap[c] = new_node
                curr = curr.hashmap[c]
        curr.terminal = True
                

    def search(self, word: str) -> bool:
        return self.helper(self.root, word, 0)

    def helper(self, node, word, index):
        curr = node
        for i in range(index, len(word)):
            if word[i] in curr.hashmap:
                curr = curr.hashmap[word[i]]
            elif word[i] == '.':
                found = False
                for entry in curr.hashmap.values():
                    if self.helper(entry, word, i + 1):
                        found = True
                return found
            else:
                return False

        return curr.terminal == True
                    