class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        pq = [(-maxMoves, 0)]
        visited = set()
        ans = 0
        while pq:
            movesLeft, u = heappop(pq)
            if u in visited: continue
            visited.add(u)
            ans += 1
            movesLeft = -movesLeft
            for v in graph[u]:
                if v not in visited and movesLeft >= graph[u][v] + 1: 
                    # This +1 which is additional move required to move from node u to node v. 
                    # since every time you traverse an edge, you consume one move.
                    # because we are traversing on edges
                    nextMoves = movesLeft - graph[u][v] - 1
                    heappush(pq, (-nextMoves, v))
                moves = min(movesLeft, graph[u][v])
                graph[u][v] -= moves
                graph[v][u] -= moves
                ans += moves
        return ans

            