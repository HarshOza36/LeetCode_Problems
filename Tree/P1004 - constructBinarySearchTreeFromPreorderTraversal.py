# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if(len(preorder) <= 0):
            return None
        
        root_val = preorder[0]
        rst_start_idx = len(preorder)
        for i, v in enumerate(preorder[1:]):
            if(v > root_val):
                rst_start_idx = i+1
                break
        
        lst = self.bstFromPreorder(preorder[1:rst_start_idx])
        rst = self.bstFromPreorder(preorder[rst_start_idx:])
        
        return TreeNode(root_val, lst, rst)