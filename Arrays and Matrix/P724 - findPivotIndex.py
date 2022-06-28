class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])

        lp = len(prefix_sum)
        left_sum = 0
        for i in range(lp):
            right_sum = prefix_sum[-1] - prefix_sum[i] if(i+1 < lp) else 0
            
            if(left_sum == right_sum):
                return i
            left_sum = prefix_sum[i]
        return -1