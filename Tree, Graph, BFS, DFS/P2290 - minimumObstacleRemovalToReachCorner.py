class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # We can make a graph where, if from (i, j) to (x, y) if we hit obstacle value is 1 else 0
        # then we just find shortest path from 0, 0 to m-1, n-1
        m, n = len(grid), len(grid[0])
        graph = defaultdict(dict)

        for i in range(m):
            for j in range(n):
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = x+i, y+j
                    if  0 <= r < m and 0 <= c < n:
                        u = (i, j)
                        v = (r, c)
                        w = grid[r][c]
                        graph[u][v] = w
        
        pq = [(0, 0, 0)]
        visited = set()
        while pq:
            dist, i, j = heappop(pq)
            if i == m-1 and j == n-1:
                return dist
            if (i, j) in visited: continue
            visited.add((i, j))
            for v in graph[(i, j)]:
                if v not in visited:
                    heappush(pq, (dist + graph[(i, j)][v], v[0], v[1]))

        return 0
                     