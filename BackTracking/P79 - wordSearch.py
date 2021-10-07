class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def solve(i, j, k):
            nonlocal board, word, is_visited, m, n, w
            if i < 0 or j < 0 or i >= n or j >= m or k >= w or is_visited[i][j] or board[i][j] != word[k]:
                return False
            
            if(k == w - 1):
                return True
            
            is_visited[i][j] = True
            
            # Checking Down, Up, Right and Left for the next letter in the word
            if solve(i, j+1, k+1) or solve(i, j-1, k+1) or solve(i+1, j, k+1) or solve(i-1, j, k+1):
                return True
            
            # Backtracking step
            is_visited[i][j] = False
            
            return False
            
        
        m, n, w = len(board[0]), len(board), len(word)
        is_visited = [[0] * m for _ in range(n)] 
        
        for i in range(n):
            for j in range(m):
                if(board[i][j] == word[0]):
                    if(solve(i,j,0)):
                        return True
        return False