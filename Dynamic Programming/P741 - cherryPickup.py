class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # backtracking Solution
        # explore all path from 0,0 to n-1,n-1 and n-1,n-1 to 0,0
        # get the optimal max cherries from both path and add them to
        # get our answer
        # Gives TLE
        
#         if len(grid) == 1 and len(grid[0]) == 1:
#             return 0 if grid[0][0] == -1 else grid[0][0]
#         maxCherry = [0]

#         def backtrack2(r, c, cherrySoFar):
#             if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1:
#                 return
            
#             if r == 0 and c == 0:
#                 maxCherry[0] = max(maxCherry[0], cherrySoFar)
#                 return
#             cherry = grid[r][c]
#             grid[r][c] = 0
#             backtrack2(r-1, c, cherrySoFar + cherry)
#             backtrack2(r, c-1, cherrySoFar + cherry)
#             grid[r][c] = cherry
        
        
        
#         def backtrack(r, c, cherrySoFar):
#             if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1:
#                 return
            
#             if r == len(grid)-1 and c == len(grid[0])-1:
#                 backtrack2(r, c, cherrySoFar)
#                 return
            
#             cherry = grid[r][c]
#             grid[r][c] = 0
#             backtrack(r+1, c, cherrySoFar + cherry)
#             backtrack(r, c+1, cherrySoFar + cherry)
#             grid[r][c] = cherry
            
#         backtrack(0,0,0)
#         return maxCherry[0]

        # DP solution
        # we will have two robots going 0,0 to n-1, n-1
        # collecting cherries, because once we go up to down
        # then we come down to up, so its like up to down twice in two
        # paths, so we have 4 options, rr, rd,dr, dd for 2 robots
        
        n = len(grid)
        mem = [[[0] * n for _ in range(n)] for _ in range(n)] 

        def dp(r1, c1, r2):
            c2 = r1+c1-r2
            # since r1+c1 = r2+c2
            # because we will always move both robots one step down
            if r1 >= len(grid) or c1 >= len(grid[0]) or r2 >= len(grid) or c2 >= len(grid[0]) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                 return float('-inf')
                
                
            if mem[r1][c1][r2]!=0:
                return mem[r1][c1][r2]
            if r1 == len(grid)-1 and c1 == len(grid[0])-1:
                return grid[r1][c1]
            
            cherries = 0
            if r1 == r2 and c1 == c2:
                # if both robots reach same spot pick cherry once
                cherries += grid[r1][c1]
            else:
                cherries += grid[r1][c1] + grid[r2][c2] 
                
            
            v1 = dp(r1, c1+1, r2) #rr
            v2 = dp(r1+1, c1, r2) #rd
            v3 = dp(r1, c1+1, r2+1) #dr
            v4 = dp(r1+1, c1, r2+1) #dd
            
            cherries += max(v1, v2, v3, v4)
            mem[r1][c1][r2] = cherries
            return cherries
        ans = dp(0,0,0)
        return 0 if ans == float('-inf') else ans
            