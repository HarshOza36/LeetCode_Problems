class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] == "."):
                    continue
                else:
                    if(self.is_valid(board,board[i][j],(i,j)) == False):
                        return False
        return True
        
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