class TrieNode():
    def __init__(self,):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        visited, ans = set(), set()
        
        def dfs(r, c, word, node):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                ans.add(word)
                node.isWord = False
            
            dfs(r+1, c, word, node)
            dfs(r-1, c, word, node)
            dfs(r, c+1, word, node)
            dfs(r, c-1, word, node)
            
            visited.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(ans)