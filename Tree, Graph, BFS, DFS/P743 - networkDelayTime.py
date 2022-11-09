class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}
        for u,v,w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
            
        pq = [(0, k)]
        t = {}
        while pq:
            time, node = heapq.heappop(pq)
            if node not in t:
                t[node] = time
                if node in graph:
                    for v, w in graph[node]:
                        heapq.heappush(pq, (time + w, v))
        return max(t.values()) if len(t) == n else -1