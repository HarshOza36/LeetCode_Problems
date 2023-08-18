class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        queue = deque(num)
        carry = 0
        for i in range(len(queue)-1,-1,-1):
            k, rem = divmod(k, 10)
            
            newNum = rem + queue[i] + carry
            carry = 0
            if newNum >= 10:
                carry, newNum = divmod(newNum, 10)

            queue[i] = newNum

            if k <= 0: 
                if i > 0 and carry > 0:
                    k = carry
                    carry = 0
                else:
                    break
        

        if k > 0: carry += k

        while carry > 0:
            carry, rem = divmod(carry, 10)
            queue.appendleft(rem)
                
        return queue