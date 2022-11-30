class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])

        visited = set()
        sr, sc = entrance[0], entrance[1]
        q = collections.deque([(sr, sc, 0)])
        visited.add((sr, sc))
        ans = float('inf')
        while q:
            for i in range(len(q)):
                r, c, d = q.popleft()
                if ([r,c] != entrance) and (r == 0 or c == 0 or r == m-1 or c == n-1):
                    ans = min(ans, d)

                for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nr, nc = r+x, c+y
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or maze[nr][nc] == "+" or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1 if ans == float('inf') else ans