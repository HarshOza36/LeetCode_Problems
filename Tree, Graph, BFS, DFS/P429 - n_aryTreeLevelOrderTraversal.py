"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        ans = []
        while queue:
            currLvl, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                currLvl.append(node.val)
                for child in node.children:
                    queue.append(child)
            ans.append(currLvl)
        return ans
                