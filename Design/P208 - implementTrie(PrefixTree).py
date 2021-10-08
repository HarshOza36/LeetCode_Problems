from collections import defaultdict

class Trie:
    
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None: # TC - O(word)
        curr = self
        for c in word:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool: # TC - O(word)
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool: # TC - O(prefix)
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)