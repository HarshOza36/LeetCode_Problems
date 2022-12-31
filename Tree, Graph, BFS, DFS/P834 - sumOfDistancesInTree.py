class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # first we will find, how many nodes fall under each subtree
        # for example in first test case
        # 0 has 6 nodes, 2 has 4 nodes and 1,3,4,5 have 1 node each counting root parents itself
        # with their children respectively that will be postorder traversal

        # after that find distance of each node from the current node within that given subtree
        # by getting the depths of the children and count of children

        # so dist[i] = dist[root] - cnt[i] + (len(cnt) - cnt[i]) where cnt[i] is count of closer nodes
        # and second half is count of farther nodes

        # closer nodes means nodes going down from this position, farther being nodes which are connected
        # from its root this will be preorder traversal
        if not edges:
            return [0] * n

        ans = [0] * n
        cnt = [0] * n

        # creating the adjacency list 
        tree = collections.defaultdict(set)
        for par, child in edges:
            tree[par].add(child)
            tree[child].add(par)

        def postOrder(root, prev):
            for node in tree[root]:
                if node == prev:
                    continue # to prevent cycle
                postOrder(node, root)
                cnt[root] += cnt[node]
                ans[root] += ans[node] + cnt[node]
            cnt[root] += 1

        def preOrder(root, prev):
            for node in tree[root]:
                if node == prev:
                    continue # to prevent cycle
                ans[node] = ans[root] - cnt[node] + (len(cnt) - cnt[node])
                preOrder(node, root)
        
        postOrder(0, -1)
        preOrder(0, -1)
        return ans

