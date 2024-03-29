class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        # idea being 0^1^0 = 1, meaning duplicate numbers exor is 0
        # else we get the number
        # we have [0,1,2,3] if n=3 and input is [3,0,1]
        # we exor all these elemnts, to get 2
        
        # we can do this in one loop as we iterate through
        # we can exor the elements of array with the indexes
        
        for i in range(len(nums)):
            ans = ans ^ i ^ nums[i]
        return ans^len(nums)
    
        # another solution is n(n+1)/2 that is sum of n numbers 
        # if we do n(n+1)/2 - sum( current nums array) we will get
        # missing number
