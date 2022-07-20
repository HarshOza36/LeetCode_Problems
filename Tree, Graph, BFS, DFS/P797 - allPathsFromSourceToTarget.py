class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
          # Recursive
#         n = len(graph)
#         visited = [False] * n
#         ans = []
#         def dfs(source, target, path):
#             if source == target:
#                 ans.append(path)
#                 return
#             visited[source] = True
#             for node in graph[source]:
#                 if not visited[node]:
#                     dfs(node, target, path + [node])
#             visited[source] = False
#         dfs(0, n-1, [0])
#         return ans
    
        # Iterative
        n = len(graph)
        stack = [0]
        ans = []
        path = []
        while stack:
            node = stack[-1]
            if(len(path) > 0 and node == path[-1]):
                path.pop()
                stack.pop()
                continue
                
            path.append(node)
            
            if(node == n-1):
                ans.append(path.copy())
                path.pop()
                stack.pop()
                continue
                
            
            for c in graph[node]:
                stack.append(c)
        return ans