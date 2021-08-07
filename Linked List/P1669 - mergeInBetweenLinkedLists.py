# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        front = list1
        i = 1
        while(i < a):
            front = front.next
            i += 1
        
        back = front.next
        front.next = list2
        
        while(list2.next != None):
            list2 = list2.next
        i = 1
        while(i < b-a+1):
            back = back.next
            i += 1
        
        list2.next = back.next        
        return list1