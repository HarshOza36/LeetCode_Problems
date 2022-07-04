class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Creating Adjacency List and Applying DFS in O(E+V) time
        # def dfs(v, visited):
        #     stack = []
        #     stack.append(v)
        #     while(stack):
        #         s = stack.pop()
        #         if(not visited[s]):
        #             visited[s] = True
        #         if s in graph:
        #             for node in graph[s]:
        #                 if(not visited[node]):
        #                     stack.append(node)
        # graph = {}
        # for i in range(len(edges)):
        #     if(edges[i][0] in graph):
        #         graph[edges[i][0]].append(edges[i][1])
        #         if(edges[i][1] in graph):
        #             graph[edges[i][1]].append(edges[i][0])
        #         else:
        #             graph[edges[i][1]] = [edges[i][0]]
        #     else:
        #         graph[edges[i][0]] = [edges[i][1]]
        #         graph[edges[i][1]] = [edges[i][0]]
        # if(n == 0):
        #     return 0
        # visited = [False for i in range(n)]
        # cnt = 0
        # for v in range(len(graph)):
        #     if(not visited[v]):
        #         dfs(v, visited)
        #         cnt += 1
        # return cnt

        # Using union find like graph parent structure and counting the parents.
        # if(n == 0): return 0
        # parent = [i for i in range(n)] # initially every node is parent of itself
        # for i in range(len(edges)):
        #     component = edges[i][1]
        #     curr_parent = edges[i][0]
        #     if(parent[curr_parent] != curr_parent):
        #         parent[component] = parent[curr_parent]
        #     else:
        #         parent[component] =  curr_parent
        # return len(set(parent))

        # Using Proper Union Find
        if(n == 0):
            return 0
        parent = [i for i in range(n)] # initially every node is parent of itself
        rank = [1] * n # initially rank of each node is 1(meaning number of nodes it is parent of.)
   
        # find parent
        def find(node):
            while node != parent[node]: # node != parent of itself ie the root parent
                parent[node] = parent[parent[node]] # path compression setting parent of our current result pointer to its grandparent so we don't have to traverse all intermediate nodes again , it is an optimization technique for union find
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if(p1 == p2):
                # parents are same no need to perform union
                return 0

            # whichever parent has higher rank we will add other parent to the higher one.
            if(rank[p2] > rank[p1]):
                parent[p1] = p2 # parent of p1 is p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1 # parent of p2 is p1
                rank[p1] += rank[p2]
            return 1 # performed union successfully

        ans = n # number of components at start
        for n1, n2 in edges:
            ans -= union(n1, n2) # if two components successfully merge then we decrement one else zero
        return ans

print(Solution().countComponents(5,[[0,1],[1,2],[3,4]]))
            
