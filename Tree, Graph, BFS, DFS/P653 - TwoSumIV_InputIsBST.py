# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def dfs(root, seen):
            if root == None: 
                return False
            complement = k - root.val
            if complement in seen: 
                return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        return dfs(root, set())