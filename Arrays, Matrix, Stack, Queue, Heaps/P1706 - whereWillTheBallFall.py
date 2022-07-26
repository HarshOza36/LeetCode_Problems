class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # O(mn) time
        m, n = len(grid), len(grid[0])
        ans = []
        for c in range(n):
            x = c
            for r in range(m):
                slope = grid[r][x]
                x += grid[r][x]
                if x < 0 or x >= n or grid[r][x] != slope:
                    ans.append(-1)
                    break    
            else:        
                ans.append(x)
        return ans