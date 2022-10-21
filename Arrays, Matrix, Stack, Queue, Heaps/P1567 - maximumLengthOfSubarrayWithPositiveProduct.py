class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        count_0 = 0
        count_neg = 0
        temp = []
        ans = float(-inf)
        for n in nums:
            if n == 0:
                ans = max(ans, self.calcLength(temp, count_neg))
                temp = []
                count_neg = 0
            else:
                if n < 0:
                    count_neg += 1
                temp.append(n)
        ans = max(ans, self.calcLength(temp, count_neg))
        return ans
        
    def calcLength(self, nums, count_neg):
        
        if count_neg % 2 == 0:
            return len(nums)
        else:
            l = 0
            r = len(nums) - 1
            while l <= r:
                if nums[l] < 0 or nums[r] < 0:
                    break
                l += 1
                r -= 1
            return r # or could return len(nums) - l

            