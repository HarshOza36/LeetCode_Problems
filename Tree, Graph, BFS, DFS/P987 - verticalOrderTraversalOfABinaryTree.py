# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dictionary will say every nodes (col,row)
        nodes = defaultdict(list)
        
        # filling the nodes with the col, row
        queue = deque([(root, (0, 0))])
        while queue:
            node, pos = queue.popleft()
            col, row = pos
            if not node: continue
            nodes[pos].append(node.val)
            queue.append((node.left, (col-1, row+1)))
            queue.append((node.right, (col+1, row+1)))
        
        # Now we will sort the nodes in nodes dictionary
        # sorted by col if tie, by row
        sorted_nodes = sorted(nodes.keys())
        ans = []
        
        for i,k in enumerate(sorted_nodes):
            # firstly, if a node say (2,0) has multiple values
            # they should be sorted by values
            nodes[k].sort()
            # if, curr col(k[0]) == prev col(sorted_nodes[i-1][0]), we need to 
            # extend values in that ans array index
            
            if i > 0 and k[0] == sorted_nodes[i-1][0]:
                ans[-1].extend(nodes[k])
            else:
                ans.append(nodes[k])
        return ans