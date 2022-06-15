class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0]
        for num in nums:
            ans += [i ^ num for i in ans]
        return sum(ans)
       