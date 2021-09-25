class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        visited = set()
        queue.append((0,0,0,k))
        
        if(k >= m + n - 2):
            return m + n - 2
        
        while queue:
            steps, x, y, k = queue.pop(0)
            if((x,y) == (n-1 ,m-1)):
                return steps
            
            for dx,dy in (x,y-1), (x,y+1), (x-1,y), (x+1,y):
                if(0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0):
                    nxt = (dx, dy, k - grid[dy][dx])
                    if(nxt not in visited):
                        visited.add(nxt)
                        queue.append((steps + 1,) + nxt)
        return -1
        