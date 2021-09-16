# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if(root == None):
            return 0
        else:
            if(root.val in range(low,high+1)):
                self.count += root.val
            
            if(root.left): self.rangeSumBST(root.left,low,high)
            if(root.right): self.rangeSumBST(root.right,low,high)
        return self.count