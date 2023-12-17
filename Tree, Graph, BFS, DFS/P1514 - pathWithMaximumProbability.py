class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
        
        pq = [(-1, start_node)]
        heapify(pq)
        visited = set()
        while pq:
            prob, node = heappop(pq)

            if node == end_node: return -prob
            visited.add(node)

            for v, w in graph[node]:
                if v not in visited:
                    heappush(pq, (prob * w, v))
        return 0
        