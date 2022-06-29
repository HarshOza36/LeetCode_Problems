# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(n) space and time
#         prev = {}
#         fast = head
#         p = None
#         while fast.next:
#             prev[fast] = p
#             p = fast
#             fast = fast.next
#         prev[fast] = p
            
#         slow = head
#         while slow != fast:
#             if(slow.val != fast.val):
#                 return False
#             slow = slow.next
#             fast = prev[fast]
#         return True

        # O(n) time O(1) space
        
        def getMiddle(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
            return slow
        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        if(head is None): return True
        
        mid = getMiddle(head)
        second_half_start = reverse(mid.next)
        ans = True
        first = head
        second = second_half_start
        while ans and second:
            if(first.val != second.val):
                ans = False
            first, second = first.next, second.next
        
        # restore list in normal state
        mid.next = reverse(second_half_start)
        return ans
