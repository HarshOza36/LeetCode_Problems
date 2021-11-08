# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        ans = 0
        while stack:
            temp = stack.pop()
            if(temp.right):
                stack.append(temp.right)
            if(temp.left and not (temp.left.left or temp.left.right)):
                ans += temp.left.val
            elif temp.left:
                stack.append(temp.left)
        return ans