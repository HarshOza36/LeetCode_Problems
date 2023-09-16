class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(list)
        for u,v in redEdges:
            graph[u].append(('r', v))

        for u,v in blueEdges:
            graph[u].append(('b', v))

        queue = collections.deque([('', 0, 0)])

        ans = [float("inf")] * (n)
        visited = set()
        while queue:
            color, node, dist = queue.popleft()
            nextColor = 'b' if color == 'r' else 'r' if color == 'b' else ''
            ans[node] = min(dist, ans[node])

            for clr, nei in graph[node]:
                if (color == "" or clr == nextColor) and (clr, nei) not in visited:
                    queue.append((clr, nei, dist + 1))
                    visited.add((clr, nei))
        return [-1 if v == float("inf") else v for v in ans] 
        