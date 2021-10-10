class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # Checking two conditions
     

        # A corollary is that, any rectangle inside the board with corners top left, top right, bottom left, 
        # bottom right must be 4 zeros or 2 ones 2 zeros or 4 zeros.
        # For example if there is a row 01010011 in the board, any other row must be either 01010011 or 10101100.
        # The same for columns

        # every row and column has half ones. Assume the board is N * N:
        # If N = 2*K, every row and every column has K ones and K zeros.
        # If N = 2*K + 1, every row and every column has K ones and K + 1 zeros or K + 1 ones and K zeros.

        N = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(N) for j in range(N)): 
            return -1
        if not N / 2 <= sum(board[0]) <= (N + 1) / 2: 
            return -1
        if not N / 2 <= sum(board[i][0] for i in range(N)) <= (N + 1) / 2:
            return -1
        col = sum(board[0][i] == i % 2 for i in range(N))
        row = sum(board[i][0] == i % 2 for i in range(N))
        if N % 2:
            if col % 2: col = N - col
            if row % 2: row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) // 2