class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[-1]*(n+1) for _ in range(m+1)]

        def dfs(r, c, prev, visited):
            if r < 0 or c < 0 or r >= m or c >= n or prev >= matrix[r][c] or (r,c) in visited:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]

            visited.add((r, c))
            
            left = 1 + dfs(r, c-1, matrix[r][c], visited)
            top = 1 + dfs(r-1, c, matrix[r][c], visited)
            right = 1 + dfs(r, c+1, matrix[r][c], visited)
            bottom = 1 + dfs(r+1, c, matrix[r][c], visited)
            visited.remove((r, c))

            dp[r][c] = max(left, top, right, bottom)
            return dp[r][c]
          
        
        maxPath = -float(inf)
        for i in range(m):
            for j in range(n):
                pathVal = dfs(i, j, -1, set())
                maxPath = max(maxPath, pathVal)
        return maxPath
