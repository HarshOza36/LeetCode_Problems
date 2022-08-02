from typing import (
    List,
)
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
##        # Bruteforce, at every location, will run DFS
##        # will run O(mn)^2 because one dfs is O(mn)
##        INF = 2147483647
##        r,c  = len(rooms), len(rooms[0])
##        visited = [[False]*c for _ in range(r)]
##
##        def dfs(i, j, steps):
##            if i < 0 or j < 0 or i >= r or j >= c or visited[i][j] or rooms[i][j] == -1:
##                return INF
##            
##            if rooms[i][j] == 0:
##                return steps
##            visited[i][j] = True
##            m1 = dfs(i + 1, j, steps + 1)
##            m2 = dfs(i, j + 1, steps + 1)
##            m3 = dfs(i - 1, j, steps + 1)
##            m4 = dfs(i, j - 1, steps + 1)
##
##            visited[i][j] = False
##            return min(m1,m2,m3,m4)
        
##        for i in range(r):
##            for j in range(c):
##                if rooms[i][j] == INF:
##                    if not visited[i][j]:
##                        rooms[i][j] = dfs(i, j, 0)
##        return rooms


        # A better solution is BFS from all the gates
        # we will simultaneously run BFS from all gates
        # it will mark the neighbours 1 distance
        # then simultaneously run BFS from 1 distance which will mark neighbours 2
        # we will keep track of visited nodes, so every expansion of BFS layers
        # we will have the closest gates
        # Hence this solution is O(mn) solution
        r, c = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def bfs(i, j):
            if i < 0 or j < 0 or i >= r or j >= c or (i,j) in visited or rooms[i][j] == -1:
                return
            visited.add((i,j))
            q.append((i,j))

        # adding all the gates
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))

        dist = 0
        while q:
            # 0th layer of queue starts from gate
            # next after expansion we will start from 1 dist rooms
            for k in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = dist

                # Now expanding for all neightbours
                bfs(i + 1, j)
                bfs(i, j + 1)
                bfs(i - 1, j)
                bfs(i, j - 1)
            dist += 1

        return rooms
    
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(Solution().wallsAndGates(rooms))
