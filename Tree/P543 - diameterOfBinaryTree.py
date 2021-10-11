# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            nonlocal diameter
            if not root: 
                return 0

            # Get Max Depth
            left = depth(root.left) if(root.left) else 0
            right = depth(root.right) if(root.right) else 0

            # Calculate diameter
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        
        diameter = 0
        depth(root)
        return diameter