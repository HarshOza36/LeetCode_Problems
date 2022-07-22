class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        preSum = 0
        seen = {0:1}
        for n in nums:
            preSum += n
            if preSum-k in seen:
                ans += seen[preSum-k]
            seen[preSum] = seen.get(preSum, 0) + 1
        return ans