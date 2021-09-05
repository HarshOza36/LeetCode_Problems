class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # Brute Force passes 66/97 and gives TLE
        # list_n = list(n)
        # count = 0
        # while True:
        #     for id, num in enumerate(list_n):
        #         if num == '0':
        #             continue
        #         else:
        #             list_n[id] = chr(ord(num)-1)
        #     count += 1
        #     if(list_n.count("0") == len(list_n)):
        #         break
        # return count

        # If we observe test cases, Number of decibinaries = max in the number
        max_ele = 0
        for i in range(len(n)):
            max_ele = max(max_ele, int(n[i]))
        return max_ele
