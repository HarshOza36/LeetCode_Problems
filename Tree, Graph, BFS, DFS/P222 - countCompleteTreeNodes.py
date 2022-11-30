# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # O(n) solution
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0

        # as asked less than O(n)
        # we will check whether a complete tree is also a full tree
        # by just comparing its left height to the right height. 
        # For a full tree we know size is 2^h-1.
        # TC =  O((logn) ^ 2) because in each iteration we need log(n) 
        # to reach leaf and count height. For each one, if it wasn't 
        # equal, we need another log(n) So worst case log(n) ^ 2.

        if not root : return 0
        left, right = root.left, root.right
        lh, rh = 1, 1
        while left: 
            left = left.left
            lh += 1
        while right: 
            right = right.right
            rh += 1
        if lh == rh : return 2**lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)