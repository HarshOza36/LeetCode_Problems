class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cityConnections = {}
        for i in range(n):
            cityConnections[i] = set()
            
        for c1, c2 in roads:
            cityConnections[c1].add(c2)
            cityConnections[c2].add(c1)


        max_rank = float("-inf")
        for i in range(n):
            for j in range(n):
                if i != j:
                    city_one_connections = len(cityConnections[i])
                    city_two_connections = len(cityConnections[j])
                    curr_rank = city_one_connections + city_two_connections
                    if i in cityConnections[j]:
                        curr_rank -= 1
                    max_rank = max(max_rank, curr_rank)
        return max_rank





