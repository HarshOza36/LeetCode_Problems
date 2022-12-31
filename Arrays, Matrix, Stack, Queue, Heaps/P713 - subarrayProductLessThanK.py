class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        ans = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            
            while prod >= k:
                prod /= nums[l]
                l += 1
            
            ans += r - l + 1
        return ans