# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root, target, currPath):
            if not root:
                return
            
            if not(root.left or root.right) and root.val == target:
                currPath.append(root.val)
                ans.append(currPath[:])
                currPath.pop()
                return
            
            target -= root.val
            currPath.append(root.val)
            dfs(root.left, target, currPath)
            dfs(root.right, target, currPath)
            currPath.pop()
            
        dfs(root, targetSum, [])
        return ans
        