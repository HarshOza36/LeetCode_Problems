class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force O(n^2)
        # ans = -float(inf)
        # for i in range(len(nums)):
        #     currSum = 0
        #     for j in range(i, len(nums)):
        #         currSum += nums[j]
        #         ans = max(ans, currSum)
        # return ans

        # Inplace O(n)
        # if(len(nums) == 1):
        #     return nums[0]
        # for i in range(1, len(nums)):
        #     nums[i] = max(nums[i-1] + nums[i], nums[i])
        # return max(nums)
        
        # Kadanes Algo O(n)
        # currSum, ans = 0, -float(inf)
        # for n in nums:
        #     currSum = max(currSum + n, n)
        #     ans = max(ans, currSum)
        # return ans
    
        # Follow up divide and conquer O(nlogn)
        def maxSubArray(A, L, R):
            if L > R: return -float(inf)
            mid, leftSum, rightSum, currSum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                currSum += A[i]
                leftSum = max(leftSum, currSum)
            currSum = 0
            for i in range(mid+1, R+1):
                currSum += A[i]
                rightSum = max(rightSum, currSum)
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), leftSum + A[mid] + rightSum)
        return maxSubArray(nums, 0, len(nums)-1)
