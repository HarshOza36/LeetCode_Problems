class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)

        for fr, to, pr in flights:
            graph[fr].append((to, pr))
        
        queue = deque([(0, src, k)])
        costs = [float("inf")] * n        
        while queue:
            dist, node, stop = queue.popleft()
            for nei, price in graph[node]:
                if dist + price < costs[nei]:
                    costs[nei] = dist + price
                    if stop > 0:
                        queue.append((dist + price, nei, stop - 1))
        
        return -1 if costs[dst] == float("inf") else costs[dst]