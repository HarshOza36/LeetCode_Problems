# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.isBal = True
        def helper(root):
            if not root: return 0
            l, r = helper(root.left), helper(root.right)
            if abs(l - r) > 1:
                self.isBal = False
            return max(l, r) + 1
        helper(root)
        return self.isBal