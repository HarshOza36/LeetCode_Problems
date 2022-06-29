# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        small = ListNode(0)
        large = ListNode(0)
        large_head = large
        ans = small
        while head:
            if(head.val < x):
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        large.next = None
        small.next = large_head.next
        return ans.next