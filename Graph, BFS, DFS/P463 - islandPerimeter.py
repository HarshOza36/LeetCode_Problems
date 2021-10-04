class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        p = 0
        
        for i in range(r):
            for j in range(c):
                if(grid[i][j]):
                    p += 4
                    
                    # If top is land then perimeter decrements by 2 because of intersection
                    if(i > 0 and grid[i - 1][j]):
                        p -= 2
                        
                    # If left is land then perimeter decrements by 2 because of intersection
                    if(j > 0 and grid[i][j - 1]):
                        p -= 2
        return p