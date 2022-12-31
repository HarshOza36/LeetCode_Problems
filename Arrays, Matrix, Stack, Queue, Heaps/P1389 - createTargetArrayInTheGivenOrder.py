class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            idx = index[i]
            val = nums[i]
            target.insert(idx,val)
        return target
