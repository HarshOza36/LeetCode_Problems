# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def inorder(root):
#             return inorder(root.left) + [root.val] + inorder(root.right) if root else []
#         # inorder will give is ascending order elements in a BST
#         a = inorder(root)
#         for i in range(1, len(a)):
#             if(a[i-1] >= a[i]):
#                 return False
#         return True

#        # above is two pass lets do it in one pass
#        lower, upper = float('-inf') , float('inf')
#        return self.dfs(lower, root, upper)
#    
#    def dfs(self, lower, root , upper):
#        
#        if root is None:
#            return True 
#        
#        if lower < root.val < upper:
#            return self.dfs(lower, root.left, root.val) and self.dfs(root.val, root.right, upper)
#        else:
#            return False

    # More concise
    def check(root,low,high):
            if(not root): return True
            if(root.val <= low or root.val >= high): return False
            return check(root.left, low, root.val) and check(root.right, root.val, high)
        return check(root, float("-inf"), float("inf"))

        
