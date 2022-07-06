"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursive
        ans = []
        def helper(root):
            if not root:
                return
            ans.append(root.val)
            for c in root.children:
                helper(c)
        helper(root)
        return ans
            
        
        # Iterative
        # if not root:
        #     return
        # stack = [root]
        # ans = []
        # while stack:
        #     node = stack.pop()
        #     ans.append(node.val)
        #     children = node.children
        #     for c in range(len(children) -1, -1, -1):
        #         stack.append(children[c])
        # return ans