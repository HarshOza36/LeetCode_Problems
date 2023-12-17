class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_row, start_col = ball
        dest_row, dest_col = hole
        
        distances = [[[float('inf'), "z"*m] for _ in range(n)] for _ in range(m)]
        distances[start_row][start_col][0] = 0
        
        pq = [(0, "", start_row, start_col)]
        heapify(pq)
        while pq:
            dist, pattern, row, col = heappop(pq)
            
            if [row, col] == hole: return pattern
                
            for x, y, dirr in [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]:
                r, c = row+x, col+y
                
                count = 0
                
                # rolling till we hit the wall in same direction
                while 0 <= r < m and 0 <= c < n and maze[r][c] != 1:
                    count += 1
                    
                    # we will check if the first r, c itself is the hole
                    if [r, c] == hole: break
                    r += x
                    c += y
                else:
                    # deduct x and y, because last while will add it.
                    r -= x
                    c -= y
                    
                    # just to check if we are not at the same start location, otherwise, we will get 
                    # wrong path.
                    if r == row and c == col: continue
                
                newDist = dist + count
                newPattern = pattern + dirr
                if [newDist, newPattern] < distances[r][c]:
                    distances[r][c] = [newDist, newPattern]
                    heappush(pq, (newDist, newPattern, r, c))
        return "IMPOSSIBLE"
    