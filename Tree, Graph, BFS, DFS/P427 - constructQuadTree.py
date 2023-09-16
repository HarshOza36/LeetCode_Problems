"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.buildQuadTree(grid, 0, 0, n)

    def buildQuadTree(self, grid, x, y, halfLine):
        if halfLine == 1:
            return Node(grid[x][y] == 1, 1)
            
        halfLine //= 2
        
        topLeft = self.buildQuadTree(grid, x, y, halfLine)
        topRight = self.buildQuadTree(grid, x, y + halfLine, halfLine)
        bottomLeft = self.buildQuadTree(grid, x + halfLine, y, halfLine)
        bottomRight = self.buildQuadTree(grid, x + halfLine, y + halfLine, halfLine)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
            if topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, 1)
        
        return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)
