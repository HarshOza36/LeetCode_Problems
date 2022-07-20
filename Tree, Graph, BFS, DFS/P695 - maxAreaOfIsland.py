class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        r,c = len(grid), len(grid[0])
        visited = [[False]*c for _ in range(r)]
        ans = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= r or j >= c or visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans