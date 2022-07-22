# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        prev = temp = ListNode(None)
        temp.next = head
        
        # Structure
        # None     ->  1 > 2 -> 3 -> 4 -> 5 -> None
        # Temp, Prev
        # reaching left
        for _ in range(left - 1):
            prev = prev.next
        tail = prev.next
        
        # Structure
        # None ->  1 -> 2 -> 3 -> 4 -> 5 -> None
        # Temp    Prev Tail
        
        for _ in range(right - left):
            nxt = prev.next
            prev.next = tail.next
            tail.next = tail.next.next
            prev.next.next = nxt
        return temp.next
            