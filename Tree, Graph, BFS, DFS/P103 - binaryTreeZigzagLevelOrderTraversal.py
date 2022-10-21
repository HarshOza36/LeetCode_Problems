# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        q = deque([root])
        ans = []
        l_to_r = True
        while q:
            currLvl, size = [], len(q)

            for i in range(size):
                node = q.popleft()

                currLvl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            if l_to_r:
                ans.append(currLvl)
                l_to_r = False
            else:
                ans.append(currLvl[::-1])
                l_to_r = True
        return ans