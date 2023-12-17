class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # we will use bit manipulation to track our visiting.
        # final state will be 111 if we have 3 nodes or 1111 if we have 4 nodes
        # in this way we are starting bfs from all nodes. say we start from 001 that is 0th node
        # when we reach 1 we will update bits to 011 that is visiting 1st node.
        
        # looking at the constraints where n = 12 maximum, we can use bit manipulation
        # now for BFS, we will use {currNode, state} thats is like {0, 001} when we reach say 1
        # we will have  {1, 011}. In this way we can protect infinite loops because now say
        # we go to 0 from 1 to get {0, 011} and 0 goes to 1 with {1, 011} then, we know we visited
        # 1 already and we dont need to go there.

        if len(graph) == 1:
            return 0

        finalState = (1 << len(graph)) - 1 # 2**n - 1 will be the final state to include all nodes

        queue = collections.deque([])

        # appending {currNode, state}
        for i in range(len(graph)):
            queue.append((i, 1 << i))

        visited = [[0] * (finalState + 1) for _ in range(len(graph))]

        shortestPath = 0
        while queue:
            n = len(queue)
            shortestPath += 1

            for i in range(n):
                node, visitedState = queue.popleft()
                
                for nei in graph[node]:
                    newVisitedState = visitedState | (1 << nei)

                    if visited[nei][newVisitedState]: continue
                    visited[nei][newVisitedState] = 1
                    if newVisitedState == finalState: return shortestPath
                    queue.append((nei, newVisitedState))
        return -1