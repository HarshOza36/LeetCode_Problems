class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # this is same house robber 1, but here since there is a cycle
        # we have 2 subproblems formed
        # Rob houses from 0 to n - 2 or Rob houses 1 to n - 1.
        # that is skip last house or skip first house
        # one edge case remains, where we just have one house
        # hence we add nums[0]
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        secondLast, prev = 0, 0
        for n in nums:
            dp =  max(n + secondLast, prev)
            secondLast = prev
            prev = dp
        return prev