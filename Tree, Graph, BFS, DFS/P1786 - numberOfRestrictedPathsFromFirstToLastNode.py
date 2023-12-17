class Solution
    def countRestrictedPaths(self, n int, edges List[List[int]]) - int
        MOD = 10  9 + 7
        graph = defaultdict(dict)
        
        for u, v, w in edges
            graph[u][v] = graph[v][u] = w
        
        dist = [float('inf')]  (n+1)
        dist[n] = 0
        pq = [(0, n)]

        while pq
            d, u = heappop(pq)
            if d  dist[u] continue
            for v in graph[u]
                if dist[v]  dist[u] + graph[u][v]
                    dist[v] = dist[u] + graph[u][v]
                    heappush(pq, (dist[v], v))
        
        @lru_cache(None)
        def dfs(src)
            if src == n return 1
            ans = 0
            for nei in graph[src]
                if dist[src]  dist[nei]
                    ans = (ans + dfs(nei)) % MOD
            return ans

        return dfs(1)