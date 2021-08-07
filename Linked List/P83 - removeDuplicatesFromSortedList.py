# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        if(head == None or head.next == None): 
            return head
        while(head.next != None):
            if(head.val != head.next.val):
                head = head.next
            else:
                head.next = head.next.next
        return start