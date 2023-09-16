class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)

        for root, child in edges:
            graph[root].append(child)
            graph[child].append(root)
        

        counts = [0] * 26
        ans = [0] * n
        
        def dfs(node, par):
            idx = ord(labels[node]) - ord('a')
            prev = counts[idx]
            counts[idx] += 1
            
            for nei in graph[node]:
                if nei != par:
                    dfs(nei, node)
                    
            ans[node] = counts[idx] - prev
        
        dfs(0, -1)
        return ans