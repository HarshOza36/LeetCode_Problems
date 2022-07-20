class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(i, j, visited, prevHeight):
            if (i, j) in visited or i < 0 or j < 0 or i == r or j == c or heights[i][j] < prevHeight:
                return 
            visited.add((i,j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
        
        
        # we will check top row for pacific and bottom for atlantic
        # from there we will see which cells we can reach as per height
        # say if we had 3 cells 1,3,5, hence from 1 we can reach 5
        # so all of them are connected to that ocean
        
        # then we will check first col and last col
        for j in range(c):
            dfs(0, j, pac, heights[0][j])
            dfs(r-1, j, atl, heights[r-1][j])
        
        for i in range(r):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, c-1, atl, heights[i][c-1])
        
        ans = []
        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in atl:
                    ans.append([i,j])
        return ans