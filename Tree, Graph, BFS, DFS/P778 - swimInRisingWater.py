class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ans = float('-inf')
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set((0, 0))
        while pq:
            val, r, c = heappop(pq)
            ans = max(ans, val)
            if r == m-1 and c == n-1: 
                return ans

            for x, y in directions:
                nr, nc = r+x, c+y

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    newVal = grid[nr][nc]
                    heappush(pq, (newVal, nr, nc))

