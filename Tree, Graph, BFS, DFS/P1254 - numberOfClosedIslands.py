class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m,n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 1:
                return False
            
            grid[i][j] = 1
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i,j)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j)
                    cnt += 1
        return cnt