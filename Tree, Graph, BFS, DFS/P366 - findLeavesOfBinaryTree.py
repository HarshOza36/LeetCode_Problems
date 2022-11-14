import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root):
        # Time and Space O(N)
        ans = []

        def heightTraverse(root):
            if not root:
              return -1
            
            # we will get the height level and then just append leaves on that level in an output list
            height = max(heightTraverse(root.left), heightTraverse(root.right)) + 1 

            # basically, when we have a new level of height
            # we will create an empty list to put the node values in it
            if height >= len(ans):
              
              ans.append([])
            
            ans[height].append(root.val)
            return height

        heightTraverse(root)
        return ans

      

obj = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

print(obj.findLeaves(root))