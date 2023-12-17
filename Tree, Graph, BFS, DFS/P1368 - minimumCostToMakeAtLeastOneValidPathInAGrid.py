class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        # Using the hint we can build a graph where grid[i][j] is 
        # # connected to all four side cells with weighted edge = 0 if sign is pointing to
        # # adjacent cell else 1
        # m, n = len(grid), len(grid[0])
        # graph = defaultdict(list)

        # # creating a direction with sign map to the directions index.
        # dirr = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        # mapping_idx = {
        #     1: 3,
        #     2: 1,
        #     3: 0,
        #     4: 2
        # }
        # for i in range(m):
        #     for j in range(n):
        #         correct_idx = mapping_idx[grid[i][j]]
        #         for idx, (x, y) in enumerate(dirr):
        #             r, c = i+x, j+y
        #             if 0 <= r < m and 0 <= c < n:
        #                 if idx == correct_idx:
        #                     graph[(i, j)].append((0, r, c))
        #                 else:
        #                     graph[(i, j)].append((1, r, c))

        # # Now we can just find the shortest path to the end.
        # pq = [(0, 0, 0)]
        # heapify(pq)
        # visited = set()
        # while pq:
        #     dist, i, j = heappop(pq)
        #     if i == m-1 and j == n-1:
        #         return dist

        #     if (i, j) in visited: continue
        #     visited.add((i, j))
        #     for d, x, y in graph[(i, j)]:
        #         if (x, y) not in visited:
        #             heappush(pq, (dist + d, x, y))
        # return -1

        # We can optimize this, we were running O(2 x MN)
        m, n = len(grid), len(grid[0])
        dirr = [(0, 1), (0, -1), (1, 0), (-1, 0)] # that is 1, 2, 3, 4
        pq = [(0, 0, 0)]
        heapify(pq)
        visited = set()

        while pq:
            dist, i, j = heappop(pq)
            if i == m-1 and j == n-1:
                return dist

            if (i, j) in visited: continue
            visited.add((i, j))

            for idx, (x, y) in enumerate(dirr):
                r, c = x+i, y+j
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    if idx == grid[i][j] - 1:
                        heappush(pq, (dist, r, c))
                    else:
                        heappush(pq, (dist+1, r, c))
        return -1