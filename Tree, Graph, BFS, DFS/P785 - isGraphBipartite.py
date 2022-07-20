class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1]*n
        
        def bfs(visited, node):
            q = deque([(node, 0)]) # node, level
            while q:
                n, level = q.popleft()
                if visited[n] != -1:
                    # it was already visited
                    if level != visited[n]:
                        return False
                else:
                    visited[n] = level
                for e in graph[n]:
                    if visited[e] == -1:
                        q.append((e, level + 1))
            return True
        
        for i in range(len(graph)):
            if visited[i] == -1:
                if not bfs(visited, i):    
                    return False
        return True