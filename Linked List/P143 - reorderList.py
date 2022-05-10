# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head.next:
            # Find Middle of list and divide in two halves
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None

            # Now reverse the second half
            p, q, mid.next = mid, mid.next, None
            while q:
                p, q, p.next = q, q.next, p
            mid = p

            # Merging
            p, q = head, mid
            while q:
                temp_p, temp_q = p, q  
                p, q = p.next, q.next
                temp_p.next, temp_q.next = temp_q, p