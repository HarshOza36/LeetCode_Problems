# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head.next
        sum = 0
        while fast:
            if(fast.val != 0):
                sum += fast.val
            elif(fast.val == 0):
                slow.val = sum
                sum = 0
                if(fast.next != None):
                    slow = slow.next
            fast = fast.next
        slow.next = None
        return head