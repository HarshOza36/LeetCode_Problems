class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # each stone is an edge in a connected graph
        # if same row or col then they share a vertex
        # so we can consider len(stones) as number of vertices
        
        parent = [i for i in range(len(stones))]
        rank = [1] * (len(stones))
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            print(p1,p2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1
        cnt = 0
        
        for i in range(len(stones)):
            for j in range(len(stones)):
                print(parent, rank)
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if union(i, j):
                        cnt += 1
        return cnt