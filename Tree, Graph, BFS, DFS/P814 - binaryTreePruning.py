# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Bruteforce Accepted
#         def dfs(root):
#             if not root:
#                 return TreeNode(0), False
#             leftChild, leftHasOne = dfs(root.left)
#             rightChild, rightHasOne = dfs(root.right)
#             if leftChild.val == 0 and not leftHasOne:
#                 root.left = None
#             else:
#                 leftHasOne = True
#             if rightChild.val == 0 and not rightHasOne:
#                 root.right = None
#             else:
#                 rightHasOne = True
#             return root, (leftHasOne or rightHasOne or root.val == 1)
#         root, ones = dfs(root)
        
#         return root if ones else None
        
        # More cleaner
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left or root.right or root.val == 1:
            return root
        else:
            return None