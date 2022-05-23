# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.deepest_leafsum = 0

    def height(self, root):
        if(root == None):
            return 0
        return 1 + max(self.height(root.right),self.height(root.left)) 
                     
    def level_order(self, root, level):
        if(root == None):
               return
        if(level == 1):
            self.deepest_leafsum += root.val
        elif (level > 1):
            self.level_order(root.left, level-1)
            self.level_order(root.right, level-1)
                   
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        h = self.height(root)
        self.level_order(root, h)
        return self.deepest_leafsum
    
        