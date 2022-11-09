class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Using floyd warshalls algorithm
        distance = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0
            
        for i, j, w in edges:
            distance[i][j] = distance[j][i] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        res = {sum(d <= distanceThreshold for d in distance[i]): i for i in range(n)}
        return res[min(res)]