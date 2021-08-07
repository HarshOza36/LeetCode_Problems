# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        temp_node = ListNode(0)
        tail = temp_node
        while True:
            if(head1 == None):
                tail.next = head2
                break
            if(head2 == None):
                tail.next = head1
                break
            if(head1.val <= head2.val):
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        return temp_node.next