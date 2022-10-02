# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we have 2 options
        
        # dont take root, take other nodes and skip that level (without root)
        # when we do not want the root, we can just take max of left and 
        # max of right  subtrees and add them
        # take current root + next.next level nodes (with root)
        # when we want the root, we add the root value and take the 
        # next values without the successor root.
        
        def dfs(root):
            if not root: return (0, 0)
            L, R = dfs(root.left), dfs(root.right)
        
        # return (without Root, with Root)
            return (max(L) + max(R), root.val + L[0] + R[0])
        return max(dfs(root))
