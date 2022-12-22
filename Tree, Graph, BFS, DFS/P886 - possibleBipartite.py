class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
       
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)
        
        def find(node):
            while node != parent[node]:
               parent[node] = parent[parent[node]]
               node = parent[node]
            return node

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1


        graph = collections.defaultdict(list)
        for par, child in dislikes:
            graph[par].append(child)
            graph[child].append(par)

        for node in range(1, n + 1):
            for neighbor in graph[node]:
                if find(node) == find(neighbor):
                    return False
                # Move all the children into same set as the first child
                # so that parent and children are in diff sets
                union(graph[node][0], neighbor)
        return True
        