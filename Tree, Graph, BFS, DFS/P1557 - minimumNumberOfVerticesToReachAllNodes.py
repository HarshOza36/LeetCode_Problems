class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # the problem is cut down to finding nodes which have indegree 0
        # because these nodes cannot be reached from any other nodes
        ans = {i for i in range(n)}
        for e in edges:
            if(e[1] in ans):
                ans.remove(e[1])
        return ans