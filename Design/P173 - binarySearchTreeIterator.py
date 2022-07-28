# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.root = root
#         self.queue = collections.deque()
#         self.getInorder(self.root)
        
#     def getInorder(self, root):
#         if not root:
#             return []
        
#         self.getInorder(root.left)
#         self.queue.append(root.val)
#         self.getInorder(root.right)
    
#     def next(self) -> int:
#         return self.queue.popleft()
        

#     def hasNext(self) -> bool:
#         return len(self.queue) > 0 

# Above in the brute force, first, our operations next and hasnext are O(1)
# Bad part is we are iterating as soon as we initialize 
# for an iterator, we should iterate after doing operations
# and for the Follow up, we need O(h) space, instead of O(total nodes) space above

class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.stack = []
        
        # we will store the left side 
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left

    def next(self):
        
        # Now we will start iterating to next
        # follow up says we need avg O(1) next

        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()