# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # get left and right max, also if they are negative, 
            # we replace it with 0 by taking max of the returned values
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            
            # this is the max we take, when we use both left and right child
            # by splitting
            # say the Example 1 of leetcode
            res = max(res, root.val + leftMax + rightMax)
            
            # finally when we come to the root, we will have to select one
            # path, instead of splitting
            # like in example 2, we would have max path 15-20-7
            # but when we come back to -10, we have to select,
            # which node path after 20, do we take, to get max
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res