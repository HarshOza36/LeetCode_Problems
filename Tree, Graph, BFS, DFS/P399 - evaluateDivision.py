class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        
        for idx, (u,v) in enumerate(equations):
            graph[u].append([v, values[idx]])
            graph[v].append([u, 1/values[idx]])
        
        
        def bfs(s, d):
            visited = set()
            q = deque([[s,1]])
            while q:
                node, val = q.popleft()
                visited.add(node)
                if node == d:
                    return val
                if node in graph:
                    for nei, v in graph[node]:
                        if nei not in visited:
                            q.append([nei, val*v])
            return -1
        
        ans = []
        for source, dest in queries:
            if source in graph and dest in graph:
                ans.append(bfs(source, dest))
            else:
                ans.append(-1)
        return ans