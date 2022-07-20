class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         # DFS
#         n = len(isConnected)
#         visited = set()
        
#         def dfs(source):
#             visited.add(source)
#             for next, connect in enumerate(isConnected[source]):
#                 if connect ==  1 and next not in visited:
#                     dfs(next)
#             return
        
#         cnt = 0
#         for i in range(n):
#             if i not in visited:
#                 dfs(i)
#                 cnt += 1
#         return cnt
            
        # Trying Union find since it is connected components
        n = len(isConnected)
        parent = [i for i in range(n)] # every node is parent of itself
        rank = [1]*n 
        
        def find(node):
            while node!=parent[node]:
                # we can stop as soon as a node is parent of itself
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if(p1 == p2):
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        ans = n
        for i in range(n):
            for j in range(n):
                if(isConnected[i][j] == 1):
                    ans -= union(i,j)
        return ans