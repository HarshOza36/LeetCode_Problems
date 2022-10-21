class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Approach we will use Union Find.
        # we will create components of "==" equations and then check if "!="
        # equations violate them
        
        # To violate, if say our components are a,b,c and d,e,f
        # if we get c!=d it doesnt violate since they are in different 
        # components, but if we get b!=a it is in a same component
        
        parent = [i for i in range(26)]
        rank = [1] * 26
        
        # since we have 26 lower case characters, we form ranks and parents for each
        # where index 0 represents a and 25 represents z in 0 indexed array
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True
        
        violationCheck = []
        for eqn in equations:
            n1, n2, condition = eqn[0], eqn[3], eqn[1:3]
            
            if condition == "!=":
                violationCheck.append(eqn)
            else:
                idx1, idx2 = ord('a') - ord(n1), ord('a') - ord(n2)
                union(idx1, idx2)
        
        for eqn in violationCheck:
            n1, n2 = eqn[0], eqn[3]
            idx1, idx2 = ord('a') - ord(n1), ord('a') - ord(n2)
            if find(idx1) == find(idx2):
                return False
        return True
            
        
        