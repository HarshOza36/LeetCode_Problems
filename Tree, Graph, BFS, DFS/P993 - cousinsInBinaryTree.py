# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        bfs = [(root,None)]
        
        while bfs:
            found_x = found_y = None
            temp = []
            
            for node,parent in bfs: # Manages every level
                if(node.val == x):
                    found_x = parent
                if(node.val == y):
                    found_y = parent
                if(node.left): temp.append((node.left, node))
                if(node.right): temp.append((node.right, node))
                    
            bfs = temp
            if(found_x and found_y and found_x != found_y):
                return True
        return False