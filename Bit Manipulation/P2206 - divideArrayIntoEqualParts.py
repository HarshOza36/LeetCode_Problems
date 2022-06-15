class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Brute Force
        # freq = {}
        # for n in nums:
        #     if(n in freq):
        #         freq[n] += 1
        #     else:
        #         freq[n] = 1
        # half = len(nums)//2
        # pairs = 0
        # for k,v in freq.items():
        #     if(v%2 != 0):
        #         return False
        #     else:
        #         pairs += v//2
        # return True if half == pairs else False
    
        # Using Bit Manipulation
        nums.sort()
        for n in range(0, len(nums), 2):
            # we are seeing 2-2 numbers at a time.
            # same number when XORed gives 0, if we dont have even pairs, 
            # then it will return false
            if(nums[n] ^ nums[n+1] != 0):
                return False
        return True
                