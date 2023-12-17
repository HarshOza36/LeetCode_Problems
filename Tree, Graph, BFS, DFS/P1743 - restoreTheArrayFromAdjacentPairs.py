class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        # In this graph, start and end will just have one pair
        # so we can find the first one, and start dfs till the end
        start = None
        for k in graph:
            if len(graph[k]) == 1:
                start = k
                break

        ans = []
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            ans.append(node)
            for nei in graph[node]:
                dfs(nei)
        dfs(start)
        return ans
            
        
