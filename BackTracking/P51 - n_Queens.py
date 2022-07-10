class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."]*(n) for _ in range(n)]
        ans = []
        
        # we will place queens row wise so, we dont need to check if there is 
        # a queen in the same row, rather we will check for col and diag
        
        def isSafe(r, c):
            # checking if there is a queen above us in same col
            for i in range(r-1, -1, -1):
                if(grid[i][c] == "Q"):
                    return False
            
            # Checking front diagonal (left top to right bottom)
            i, j = r-1, c-1
            while(i >=0 and j >=0):
                if(grid[i][j] == "Q"):
                    return False
                i -= 1
                j -= 1
                
            # Checking reverse diagonal(right top to left bottom)
            i, j = r-1, c+1
            while(i >=0 and j < n):
                if(grid[i][j] == "Q"):
                    return False
                i -= 1
                j += 1
            return True
        
        def nQueens(r, path):
            if(r == n):
                ans.append(path) 
                return
            for c in range(n):
                if(grid[r][c] == "." and isSafe(r,c)):
                    grid[r][c] = "Q"
                    nQueens(r + 1, path + ["."*c + "Q" + "."*(n-c-1)])
                    grid[r][c] = "."
        nQueens(0, [])
        return ans
                