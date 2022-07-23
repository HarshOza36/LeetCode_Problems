# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # now we need to find mid of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None
        
        # Now we merge(sort(left), sort(right))
        return self.merge(self.sortList(head), self.sortList(right))
    
    def merge(self, left, right):
        if not left: return right
        elif not right: return left
        
        temp = ListNode(0)
        head = temp
        
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        
        head.next = left if not right else right
        return temp.next