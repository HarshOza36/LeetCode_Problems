# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, prevMax):
            if not root:
                return 0
            ans = 1 if root.val >= prevMax else 0
            ans += helper(root.left, max(prevMax, root.val))
            ans += helper(root.right, max(prevMax, root.val))
            return ans
        
        return helper(root, float(-inf))
