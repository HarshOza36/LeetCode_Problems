class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            # no way to form connections
            return -1
        
        parent = [i for i in range(n)] 
        rank = [1] * n 
        def find(node):
            while node != parent[node]: 
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if(p1 == p2):
                return 0

            if(rank[p2] > rank[p1]):
                parent[p1] = p2 
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1 
                rank[p1] += rank[p2]
            return 1

        ans = n 
        for n1, n2 in connections:
            ans -= union(n1, n2)
        return ans-1