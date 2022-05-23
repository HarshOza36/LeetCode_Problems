# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if(cloned == None):
            return
        if(cloned.val == target.val):
            return cloned
         
        left = self.getTargetCopy(original, cloned.left, target)
        right = self.getTargetCopy(original, cloned.right,target)
        if(left != None): return left
        if(right != None): return right
        return None