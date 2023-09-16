class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan_dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        n = len(points)
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan_dist(points[i], points[j])
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        
        cnt = 1
        ans = 0
        visited = [0] * n
        heap = graph[0]
        heapify(heap)
        visited[0] = 1

        while heap:
            dist, nei = heappop(heap)
            if not visited[nei]:
                visited[nei] = 1
                cnt += 1
                ans += dist
                for node in graph[nei]: heappush(heap, node)
            if cnt >= n: break
        
        return ans