class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        out = []
        for i in range (0,n):
            out.append(nums[i])
            out.append(nums[n+i])
        return out
    
#         Brute Force thought
#         x = nums[:n]
#         y = nums[n:]
#         # final = []
#         # for i in range(len(nums)):
#         #     if(i % 2 == 0):
#         #         final.append(x.pop(0))
#         #     else:
#         #         final.append(y.pop(0))
#         # return final
    
#         # One liner
#         return [x.pop(0) if(i % 2 == 0) else y.pop(0) for i in range(len(nums))]
