class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        toVisit = set() # grid[i][j] that we want to visit
        start = end = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    toVisit.add((i,j))
                elif(grid[i][j] == 1):
                    start = (i,j)
                elif(grid[i][j] == 2):
                    end = (i,j)
                    toVisit.add((i,j))
        
        return self.backtrack(start[0], start[1], toVisit, end)
    
    def backtrack(self, i, j, toVisit, end):
            if((i,j) == end and len(toVisit) == 0):
                return 1
            
            out = 0
            for v in (i-1,j), (i+1,j), (i,j-1),(i,j+1):
                if v in toVisit:
                    toVisit.remove(v)
                    out += self.backtrack(v[0], v[1], toVisit, end)
                    toVisit.add(v) # backtracking step
            return out