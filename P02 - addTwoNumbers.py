# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         l1_list = []
#         l2_list = []
#         while l1.next != None:
#             l1_list.append(l1.val)
#             l1 = l1.next
#         l1_list.append(l1.val)
#         while l2.next != None:
#             l2_list.append(l2.val)
#             l2 = l2.next
#         l2_list.append(l2.val)
#         output = list(str(int("".join(map(str, l1_list))) +
#                           int("".join(map(str, l2_list)))))[::-1]
#         output = list(map(int, output))
#         head = l3 = ListNode(output.pop(0))
#         for i in output:
#             l3.next = ListNode(i)
#             l3 = l3.next
#         return head

# Above is a brute force approach but it works for
# [2,4,3] [5,6,4] Output [7,0,8] since carry logic mentioned is not used properly


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = curr = ListNode()
        while l1 and l2:
            total = l1.val + l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l1, l2, curr = l1.next, l2.next, curr.next
        while l1:
            total = l1.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l1, curr = l1.next, curr.next

        while l2:
            total = l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l2, curr = l2.next, curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head.next
