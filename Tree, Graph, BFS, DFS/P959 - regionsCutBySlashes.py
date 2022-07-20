class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        # in a grid we will have NxN cells
        # corners of these each cells will be our graph vertices
        # the edges will be these slashes
        # the outer boundary of full grid will connect the vertices of cell corners
        # 0_____1_____2_____3
        # |     |     |     |
        # 4_____5_____6_____7
        # |     |     |     |
        # 8_____9_____10____11
        # |     |     |     |
        # 12____13____14____15
        # so given 3x3 grid we have 16 vertices, and the boundary
        # 0,1,2,3,7,11,15,14,13,12,8,4 are all connected with edges and parent of all 
        # of them will be 0
        # Now say a forward slash(/) in cell 0,0, will connect vertices 4 and 1
        # and so on.
        # whenever we have a cycle in a graph, region size is increased
        # by adding this one /, our regions get 2
        # 0_____1_____2_____3
        # |   / |     |     |
        # 4_/___5_____6_____7
        # |     |     |     |
        # 8_____9_____10____11
        # |     |     |     |
        # 12____13____14____15
        # if i,j is '/' we connect (i+1,j) and (i, j+1) in the graph
        # if i,j is '\\' we connect (i,j) and (i+1, j+1) in the graph
        # for example 0,0 was '/' so we connect (1,0) and (0,1) in graph which are
        # vertex 4, 1, to get vertex, we will do, r*(n+1) + c where n is len(input grid)
        
        # Hence we will use union find, and whenever we find a cycle , we increment count
        # of regions
        
        
        n = len(grid)
        parent = [i for i in range((n+1)**2)]
        lp = len(parent)
        rank = [1]*((n+1)**2)
        
        # set parent of all border elements to 0
        for i in range(lp):
            # top row or left col or right col or bottom row
            if 0 <= i <= n or i % (n+1) == 0 or i % (n+1) == n or i >= lp-1-n:
                rank[0] += rank[i]
                parent[i] = 0

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if(rank[p2] > rank[p1]):
                rank[p2] += rank[p1]
                parent[p1] = p2
            else:
                rank[p1] += rank[p2]
                parent[p2] = p1
            return True
        region = 1
        for r,row in enumerate(grid):
            for c,ch in enumerate(row):
                if ch == '/':
                    i1, j1 = r, c+1
                    i2, j2 = r+1,c
                    v1, v2 = i1*(n+1) + j1, i2*(n+1) + j2 
                    if not union(v1, v2):
                        region += 1
                elif ch == '\\':
                    i1, j1 = r, c
                    i2, j2 = r+1,c+1
                    v1, v2 = i1*(n+1) + j1, i2*(n+1) + j2 
                    if not union(v1, v2):
                        region += 1
        return region
                    
        