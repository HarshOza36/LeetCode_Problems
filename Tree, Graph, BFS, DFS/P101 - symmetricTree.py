# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return helper(L.left, R.right) and helper(L.right, R.left)
        return helper(root.left, root.right)
        