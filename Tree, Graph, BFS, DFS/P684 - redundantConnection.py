class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         # DFS O(n^2)  
#         graph = collections.defaultdict(set)

#         def dfs(source, target):
#             if source not in seen:
#                 seen.add(source)
#                 if source == target: return True
#                 return any(dfs(n, target) for n in graph[source])

#         for u, v in edges:
#             seen = set()
#             if u in graph and v in graph and dfs(u, v):
#                 return u, v
#             graph[u].add(v)
#             graph[v].add(u)


        # Using Union Find
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                parent[p1] = p2
            else:
                rank[p1] += rank[p2]
                parent[p2] = p1
            return 1
        
        for u,v in edges:
            if(not union(u,v)):
                # that means parent of these two vertices is same vertex
                return [u,v]
                