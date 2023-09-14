class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        maxf = l = 0
        count = defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]] += 1
            maxf = max(maxf, count[nums[r]])
            if r - l + 1 - maxf > k:
                count[nums[l]] -= 1
                l += 1
        return maxf
