class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph = collections.defaultdict(list)
        for root, child in edges:
            graph[root].append(child)
            graph[child].append(root)

        
        steps = 0
        visited = set()
        def dfs(root, dist):
            if root == 0 or root in visited:
                return dist * 2
            
            visited.add(root)
            for nei in graph[root]:
               return dfs(nei, dist + 1)
            

        for node, apple in enumerate(hasApple):
            if apple:
                steps += dfs(node, 0)
        return steps