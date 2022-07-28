# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, val1, val2):
            if not root:
                return None
            if root.val == val1 or root.val == val2:
                return root
            L = dfs(root.left, val1, val2)
            R = dfs(root.right, val1, val2)
            if L and R:
                return root
            return L if L else R
        return dfs(root, p.val, q.val)
    
#         # Iterative    
#         stack = [root]
#         parents = {root:False}
        
#         # We run DFS O(n) and keep track of all parents
#         while stack:
#             node = stack.pop()
#             if node.left:
#                 parents[node.left] = node
#                 stack.append(node.left)
#             if node.right:
#                 parents[node.right] = node
#                 stack.append(node.right)
#             if p in parents and q in parents:
#                 break
#                 # just a small optimization
#                 # because if we found both p and q, we do not need other
#                 # parents
            
#         ancestors = set()
        
#         # now we will add all ancestors of 'p' till root
#         while p:
#             ancestors.add(p)
#             p = parents[p]
        
#         # Now we will only stop, if we find 'q' in the ancestors,
#         # meaning that its parent exists in 'p's parents list
#         # hence that is the LCA
        
#         while q not in ancestors:
#             q = parents[q]
#         return q
            
        