class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if(len(moves) <= 4):
            return "Pending"
        
        # creating a board with value not useful. If i use -1 and if board row is 0,1,-1
        # the row sum is 0 and A wins, but it is wrong hence -5 a safe bet. There can be many such examples.
        board = [[-5 for j in range(3)] for j in range(3)]

        # filling board        
        curr_player = 0
        for x,y in moves:
            board[x][y] = curr_player
            curr_player = 1 if curr_player == 0 else 0
            
        # Checking main diagonal
        main_diag = board[0][0] + board[1][1] + board[2][2]
        if (main_diag == 0 or main_diag == 3): 
            print("Here md")
            return "A" if main_diag == 0 else "B"
        
        # Checking reverse diagonal
        rev_diag = board[0][2] + board[1][1] + board[2][0]
        if (rev_diag == 0 or rev_diag == 3): 
            print("Here rd")
            return "A" if rev_diag == 0 else "B"
      
        # Checking rows and cols
        for y in range(3):
            sum_row = sum_col = 0
            for x in range(3):
                sum_row += board[y][x]
                sum_col += board[x][y]
                
            if (sum_row == 0 or sum_row == 3): 
                print("Here sr")
                return "A" if sum_row == 0 else "B"
            if (sum_col == 0 or sum_col == 3):
                print("Here sc")
                return "A" if sum_col == 0 else "B"

        return "Draw" if len(moves) == 9 else "Pending"