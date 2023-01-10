class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        

        # dp[i] will store a hashmap which will have Keys as the common difference between
        # elements and values are count of APs ending at that ith point which have >= 2 elements.
        dp = [{} for i in range(len(nums))]
        ans = 0


        # now for each element we will check common difference with all elements before it
        # if we find a common difference already in the dictionary of a prev element
        # we will take value of that prev element's common diff key and +1 it into the curr element
        # common diff key
        # for example if we had 4 5 8 6 and dp = [{},{},{},{}]
        # here we start with 5 and its dp will be {1:1}
        # for 8 we will have 4-8 and 5-8 dp will be {4:1,3:1}
        # for 6 we will get 1 for 6-5 and 5 already has a 1 so dp will be {2:1,1:2} where 2:1 is from
        # 6-4. so in this way we got 4-5-6 as our first subsequence we store it in res and continue
        # this till the end

        for i in range(1, len(dp)):
            for j in range(0, i):
                commonDiff = nums[i] - nums[j]

                apEndingOnJ = dp[j].get(commonDiff, 0)
                apEndingOnI = dp[i].get(commonDiff, 0)
               
                ans += apEndingOnJ
                dp[i][commonDiff] = apEndingOnJ + apEndingOnI + 1

       
        return ans