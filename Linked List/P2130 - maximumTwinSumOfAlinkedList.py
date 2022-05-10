# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Brute force 40% faster
#         d = deque()
#         while head:
#             d.append(head)
#             head = head.next
       
#         max_val = float("-inf")
#         while d:
#             max_val = max(max_val, d.popleft().val + d.pop().val)
#         return max_val
        
        # using Slow and Fast pointers to optimise
        # Finding middle
        slow = fast = head
        prev = slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        prev = None
        
        # Reversing first part
        while head:
            nxt = head.next
            head.next = prev
            prev, head = head, nxt
            
        # Now calculating max
        max_val = float("-inf")
        while prev:
            max_val = max(max_val, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return max_val