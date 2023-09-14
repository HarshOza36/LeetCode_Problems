# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        length = self.getLength(head)
        split = length // k
        rem = length % k

        node = head
        prev = None
        for i in range(k):
            ans[i] = node
            n = split + (1 if rem > 0 else 0)

            for j in range(n):
                prev = node
                node = node.next

            if prev: prev.next = None
            if rem > 0: rem -= 1

        return ans


    def getLength(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    