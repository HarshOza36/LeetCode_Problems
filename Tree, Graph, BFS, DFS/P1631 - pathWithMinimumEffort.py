class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        effort = 0
        while pq:
            effort, x, y = heappop(pq)
            if x == m-1 and y == n-1: return effort

            for i, j in directions:
                row, col = x+i, y+j

                if 0 <= row < m and 0 <= col < n:
                    newDist = max(effort, abs(heights[row][col] - heights[x][y]))
                    if dist[row][col] > newDist:
                        dist[row][col] = newDist
                        heappush(pq, (newDist, row, col))
        return effort

                    


