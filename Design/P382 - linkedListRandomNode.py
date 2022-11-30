
# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):

#     def __init__(self, head):
#         """
#         :type head: Optional[ListNode]
#         """
#         self.head = head
#         self.size = 0
#         # O(n) time
#         while head:
#             self.size += 1
#             head = head.next

#     def getRandom(self):
#         """
#         :rtype: int
#         """
#         # O(n) time
#         randomVal = random.randint(0, self.size - 1)
#         head = self.head
#         while randomVal:
#             head = head.next
#             randomVal -= 1
#         return head.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# using Reservoir sampling to get O(1) init constructor
class Solution(object):
    def __init__(self, head):
        self.head = head

    
    def getRandom(self):  
        # cost O(n) Time
        # Reservoir sampling and K == 1
        ans = 0
        head, i = self.head, 0
        while head:
            if random.randint(0, i) == 0: 
                # capacity of the reservoir is 1, because we just need to return a single num
                ans = head.val  # replace ans with i-th node.val with probability 1/i
            head = head.next
            i += 1
        return ans