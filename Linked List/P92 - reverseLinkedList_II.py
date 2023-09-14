# Two Pass Solution
# Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         if left == right:
#             return head
        
#         leftPtr = rightPtr = leftPrevPtr = rightNextPtr = None
#         temp = head
#         count = 1
#         prev = None
#         while temp:
#             if count == left:
#                 leftPtr = temp
#                 leftPrevPtr = prev
#             elif count == right:
#                 rightPtr = temp
#                 rightNextPtr = temp.next
#                 break
#             count += 1
#             prev = temp
#             temp = temp.next

#         curr = leftPtr.next
#         prev = leftPtr

#         while curr != rightPtr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt


#         curr.next = prev
#         if leftPrevPtr: 
#             leftPrevPtr.next = rightPtr
#         else:
#             head = curr
#         leftPtr.next = rightNextPtr
#         return head
            
# One Pass Solution
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
            