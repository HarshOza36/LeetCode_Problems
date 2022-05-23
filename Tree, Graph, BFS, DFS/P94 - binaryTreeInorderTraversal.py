# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.nodes = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root == None):
            return []
        else:
            if(root.left): self.inorderTraversal(root.left)
            self.nodes.append(root.val)
            if(root.right): self.inorderTraversal(root.right)
        return self.nodes