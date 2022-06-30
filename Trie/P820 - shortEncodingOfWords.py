class TrieNode:
    def __init__(self):
        self.children = {}
        self.startOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr.startOfWord = False # it cannot be start anymore we are creating more words for this now.
            curr = curr.children[c]
        if curr.children:
            curr.startOfWord = False # because it is not start anymore, it will has more children making more words.
        else:
            curr.startOfWord = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.startOfWord

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        t = Trie()
        s = set()
        # removing duplicates and reversing words
        for w in words:
            s.add(w[::-1])

        for w in s:
            t.insert(w) # inserting all reversed, because we want ends with
        
        ans = 0
        for w in s:
            if t.search(w):
                ans += len(w) + 1
        return ans
            
        
        