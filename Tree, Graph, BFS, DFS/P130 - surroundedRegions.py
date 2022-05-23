class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n, curr = len(board), len(board[0]), deque()
       
        # get all 'O's from the border
        for i in range(n):
            if board[0][i] == 'O':  # top row
                curr.append((0, i))
            if m > 1 and board[m-1][i] == 'O':  # bottom row
                curr.append((m-1, i))
                
        for i in range(1, m-1):
            if board[i][0] == 'O':  # left column
                curr.append((i, 0))
            if n > 1 and board[i][n-1] == 'O':  # right column
                curr.append((i, n-1))
        
        # BFS
        while curr:
            i, j = curr.popleft()
            board[i][j] = 'V'  # V means visited and seen
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    curr.append((x, y))
        

        for i in range(m):
            for j in range(n):
                board[i][j] = 'X' if board[i][j] == 'O' else 'O' if board[i][j] == 'V' else board[i][j]