class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)-1
        for i in range(n,0,-1):
            if(nums[i] != nums[i-1]):
                nums.pop(i)
     
        nums.pop(0)
        return nums