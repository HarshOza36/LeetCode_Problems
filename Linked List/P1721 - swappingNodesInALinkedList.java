/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        // Just swapping values also works
        // ListNode fromStart = head;
        // for(int i=1; i<k; i++) fromStart = fromStart.next;
        // ListNode slow = head, fast = fromStart.next;
        // while(fast!=null){
        //     fast = fast.next;
        //     slow = slow.next;
        // }
        // int temp = slow.val;
        // slow.val = fromStart.val;
        // fromStart.val = temp;
        // return head;

        // But lets swap nodes instead which is correct way to solve linked list problems
        // When swapping Nodes we have 4 cases to handle
        // First two cases are normal where we can swap the nodes and set prev.next to them
        // 1. Normal prevFromStart, fromStart
        // 2. Normal prevFromEnd, fromEnd
        // Next two case are where the fromEnd.next is fromStart, or fromStart.next is fromEnd
        // 3. prevFromStart, fromStart, fromEnd
        // 4. prevFromEnd, fromEnd, fromStart

        ListNode temp = new ListNode(-1);
        temp.next = head;
        

        ListNode prevFromStart = temp, prevFromEnd = temp;
        ListNode fromStart = head, fromEnd = head;

        // Getting the kth node from start 
        for(int i=1; i<k; i++){
            prevFromStart = prevFromStart.next;
            fromStart = fromStart.next;
        }

        // Getting the kth node from end
        ListNode curr = fromStart;
        while(curr.next != null){
            prevFromEnd = prevFromEnd.next;
            fromEnd = fromEnd.next;
            curr = curr.next;
        }

        // If fromStart.next is fromEnd that is prevFromEnd == fromStart
        if(prevFromEnd == fromStart){
            // In this case we can just swap fromEnd and fromStart
            ListNode t = fromEnd.next;
            prevFromStart.next = fromEnd;
            fromEnd.next = fromStart;
            fromStart.next = t;
        }else if(prevFromStart == fromEnd){
            // If fromEnd.next is start that is prevFromStart == fromEnd
            ListNode t = fromStart.next;
            prevFromEnd.next = fromStart;
            fromStart.next = fromEnd;
            fromEnd.next = t;
        }else{
            // this is the normal case
            ListNode t = fromStart.next;
            prevFromStart.next = fromEnd;
            fromStart.next = fromEnd.next;
            prevFromEnd.next = fromStart;
            fromEnd.next = t;
        }

        return temp.next;

    }
}