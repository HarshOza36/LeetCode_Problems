class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_row, start_col = start
        dest_row, dest_col = destination
        
        distances = [[float('inf')] * n for _ in range(m)]
        distances[start_row][start_col] = 0
        
        pq = [(0, start_row, start_col)]
        heapify(pq)
        while pq:
            dist, row, col = heappop(pq)
        
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = row+x, col+y
                count = 0
                # rolling till we hit the wall in same direction
                while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                    r += x
                    c += y
                    count += 1

                # deduct x and y, because last while will add it.
                r -= x
                c -= y
                newDist = dist + count
                if newDist < distances[r][c]:
                    distances[r][c] = newDist
                    heappush(pq, (newDist, r, c))
        return -1 if distances[dest_row][dest_col] == float("inf") else distances[dest_row][dest_col]
        