# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if(root1 == None):
            return root2
        stack = []
        stack.append([root1,root2])
        while stack:
            t = stack.pop()
            if(t[0] == None or t[1] == None):
                continue
            t[0].val += t[1].val
            if(t[0].left == None):
                t[0].left = t[1].left
            else:
                stack.append([t[0].left, t[1].left])
            if(t[0].right == None):
                t[0].right = t[1].right
            else:
                stack.append([t[0].right, t[1].right])
        return root1