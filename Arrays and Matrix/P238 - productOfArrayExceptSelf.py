class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Brute Force
        # out = []
        # n = len(nums)
        # for i in range(n):
        #     temp = nums[:i] + nums[i+1:]
        #     mul = 1
        #     for j in range(len(temp)):
        #         mul *= temp[j]
        #     out.append(mul)
        # return out
        
        # Now we require O(n) time and O(1) space
        out, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            # prefix product from one end
            out[i] *= pre
            pre *= nums[i]
            # suffix product from other end
            out[-1-i] *= suf
            suf *= nums[-1-i]

        return out