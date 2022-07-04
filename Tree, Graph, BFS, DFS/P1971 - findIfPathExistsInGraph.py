class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_mat = {}
        for e1, e2 in edges:
            if e1 in adj_mat:
                adj_mat[e1].append(e2)
            else:
                adj_mat[e1] = [e2]
                
            if e2 in adj_mat:
                adj_mat[e2].append(e1)
            else:
                adj_mat[e2] = [e1]    
                
        visited = set()
        stack = [source]
        while stack:
            v = stack.pop()
            visited.add(v)
            if v in adj_mat:
                for n in adj_mat[v]:
                    if n not in visited:
                        stack.append(n)
            if(v == destination):
                return True
        return False
        