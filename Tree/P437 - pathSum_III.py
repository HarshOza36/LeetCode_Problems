# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        cache = {0:1}
        
        def dfs(root, targetSum, currPathSum, cache):
            
            if not root:
                return
            
            currPathSum += root.val
            oldPathSum = currPathSum - targetSum
            self.res += cache.get(oldPathSum, 0)
            cache[currPathSum] = cache.get(currPathSum, 0) + 1

            dfs(root.left, targetSum, currPathSum, cache)
            dfs(root.right, targetSum, currPathSum, cache)

            # withdraw selection
            cache[currPathSum] -= 1
            
        dfs(root, targetSum, 0, cache)
        return self.res
    
   
