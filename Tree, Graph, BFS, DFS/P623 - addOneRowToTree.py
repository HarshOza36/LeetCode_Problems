# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        

        def dfs(val, root, curr_depth, depth):
            if not root:
                return
            
            if curr_depth == depth-1:
                left, right = root.left, root.right
                lnode, rnode = TreeNode(val), TreeNode(val)
                root.left, root.right = lnode, rnode
                lnode.left, rnode.right = left, right
                return root
            
            dfs(val, root.left, curr_depth + 1, depth)
            dfs(val, root.right, curr_depth + 1, depth)
            return root
        
        return dfs(val, root, 1, depth)