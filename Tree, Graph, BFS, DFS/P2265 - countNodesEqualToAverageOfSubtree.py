# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def findNodes(root):
            nonlocal ans
            if not root: return 0, 0
            if not root.left and not root.right:
                ans += 1
                return root.val, 1
            left, leftCnt = findNodes(root.left)
            right, rightCnt = findNodes(root.right)
            summ, nodes = root.val + left + right, leftCnt + rightCnt + 1
            avg = summ // nodes
            if avg == root.val: ans += 1
            return summ, nodes
        findNodes(root)
        return ans