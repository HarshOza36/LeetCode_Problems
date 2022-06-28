class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Brute Force
        # arr = []
        # for i in range(n+1):
           #  binary_val = bin(i)
            # arr.append(binary_val.count("1"))
#        return arr

        # Using DP - O(n) time
        # opt = [None for i in range(n+1)]
        # opt[0] = 0
        # for i in range(1,n+1):
        #     opt[i] = opt[i//2] + i%2
        # return opt
    
        # Using Bit Manipulation - O(nlogn) time just 
#         ans = []
#         for i in range(n + 1): # runs n time
#             count = 0
#             temp = i
#             while(temp > 0): # runs logn time
#                 # we do n%2 to get the remainder if its 1 then we have one in the binary representation
                
#                 if((temp & 1) == 1):
#                     count += 1
#                 # divide number by two that is right shift by 1
#                 temp = temp >> 1
#             ans.append(count)
#         return ans
        
        # Kernighan's Algorithm - O(n)
        ans = []
        for i in range(n+1):
            cntr = 0
            while(i != 0):
                rightmost_set_bitmask = (i & -i)
                i -= rightmost_set_bitmask
                cntr += 1
            ans.append(cntr)
        return ans
            