# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.inorderTraversal = []
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if(root == None):
                return
            if(root.left): self.increasingBST(root.left)
            self.inorderTraversal.append(root.val)
            if(root.right): self.increasingBST(root.right)
            
        inorder(root)
        main_root = tree = TreeNode(0)
        for v in self.inorderTraversal:
            tree.right = TreeNode(v)
            tree = tree.right
        return main_root.right