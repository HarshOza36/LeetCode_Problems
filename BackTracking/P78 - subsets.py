class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        def helper(nums, ans):
            if len(nums) == 0:
                out.append(ans)
                return
            curr = nums[0]
            helper(nums[1:], ans)
            helper(nums[1:], ans + [curr])
        helper(nums, [])
        return out