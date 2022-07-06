# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappushpop, heappop, heapify
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # First adding all list elements into one single list
        lists = [i for i in lists if i is not None]
        if not lists:
            return None
        
        # Creating the priority queue
        pq = [(ll.val, idx, ll) for idx, ll in enumerate(lists)]
        
        # Adding elements into heap
        heapify(pq)

        _, i, curr_list = heappop(pq)

        temp = curr_list
        
        while pq:
            nxt_val, i, nxt_list = pq[0]

            # instead of poping and pushing each value one by one, we take the min list 
            # and then we set the next node to be the next smallest list
            
            while curr_list.next is not None and curr_list.next.val <= nxt_val:
                curr_list = curr_list.next

            remainder, curr_list.next = curr_list.next, nxt_list

            # adding the remainder back to heap
            if remainder is not None:
                # we push the remainder and then pop by using a single command
                _, i, curr_list = heappushpop(pq, (remainder.val, i, remainder))
            else:
                _, i, curr_list = heappop(pq)

        return temp