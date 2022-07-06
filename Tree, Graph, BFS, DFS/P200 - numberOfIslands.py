class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        visited = [[False]*c for _ in range(r)]
        
        
        def dfs(sr, sc):
            if(sr < 0 or sc < 0 or sr >= r or sc >= c or grid[sr][sc] == '0' or visited[sr][sc]):
                return
            visited[sr][sc] = True
            dfs(sr + 1, sc)
            dfs(sr, sc + 1)
            dfs(sr - 1, sc)
            dfs(sr, sc - 1)
            
        cnt = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt