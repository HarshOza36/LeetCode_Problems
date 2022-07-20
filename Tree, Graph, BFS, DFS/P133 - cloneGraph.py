"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        clones = {node : Node(node.val, [])}
        stack = [node]
        
        while stack:
            n = stack.pop()
            for nei in n.neighbors:
                if nei not in clones:
                    neiCopy = Node(nei.val, [])
                    clones[nei] = neiCopy
                    clones[n].neighbors.append(neiCopy)
                    stack.append(nei)
                else:
                    clones[n].neighbors.append(clones[nei])
        return clones[node]