# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # O(n) time and space
#         preorder = []
#         def getPre(root):
#             if not root:
#                 return 
#             preorder.append(root)
#             getPre(root.left)
#             getPre(root.right)
#         getPre(root)
        
#         for i in range(1, len(preorder)):
#             root.left = None
#             root.right = preorder[i]
#             root = root.right

        # O(1) space follow up
        if not root:
            return

        # using Morris Traversal
        curr = root

        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
