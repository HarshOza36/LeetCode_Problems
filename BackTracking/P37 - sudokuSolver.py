class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board or len(board) == 0:
            return
        self.solve(board)
        return board
        
    def pick_empty(self,board): # To pick an empty space to start with.
        for x in range(len(board)):
            for y in range(len(board)):
                if(board[x][y] == '.'):
                    return (x, y) # row,col
        
    def is_valid(self,board, num, pos): # To find if the current board is valid or not
        x, y = pos
        for i in range(len(board[0])): # Check the row
            if(board[x][i] == num and y != i): # Checking if new num is equal to any existing one
                return False

        for j in range(len(board)): # Check the col
            if(board[j][y] == num and x != j): # Checking if new num is equal to any existing one
                return False

        # Now checking the 3*3 box 
        box_x = y//3
        box_y = x//3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                  if(board[i][j] == num and (i,j) != pos):
                    return False
        return True


    def solve(self,board):
        find = self.pick_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.is_valid(board, str(i), (row,col)):
                board[row][col] = str(i)

                if self.solve(board):
                    return True

                board[row][col] = '.'

        return False
