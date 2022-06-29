# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while (p1 or p2) and p1 != p2:
            if not p1: 
                p1 = headB
            else:
                p1 = p1.next
            if not p2: 
                p2 = headA
            else:
                p2 = p2.next
            
        return p2