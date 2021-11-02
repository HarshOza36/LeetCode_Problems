"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def traverseChild(self, head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail
    
    def flatten(self, head: 'Node') -> 'Node':
        if(not head):
            return head
        temp = head
        while temp:
            if(temp.child):
                tail = self.traverseChild(temp.child)
                tail.next = temp.next
                if tail.next:
                    tail.next.prev = tail
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None   
            temp = temp.next
        return head
                