class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dp O(n^2)
        # n = len(nums)
        # dp = [0] * len(nums)
        # dp[0] = 1
        # ans = 1
        # for i in range(1, n):
        #     curr_max = float("-inf")
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             curr_max = max(curr_max, dp[j] + 1)
        #     dp[i] = curr_max if curr_max != float('-inf') else 1
        #     ans = max(ans, dp[i])
        # return ans
        
        # O(nLogn) follow up
        res = []
        
        # we will search if a number is greater than res[i]
        # if yes we will insert it in our ans
        # in such way we will keep getting elements in a sorted order
        # For example
        # ele searched_idx ans
        # 10 0 []
        # 9 0 [10]
        # 2 0 [9]
        # 5 1 [2]
        # 3 1 [2, 5]
        # 7 2 [2, 3]
        # 101 3 [2, 3, 7]
        # 18 3 [2, 3, 7, 101]

        def search(target):
            left = 0
            right = len(res)-1
            while left < right:
                mid = left + (right-left) // 2
                if target <= res[mid]:
                    right = mid
                else:
                    left = mid + 1
            return (left + 1) if left < len(res) and res[left] < target else left
        
        for num in nums:
            pos = search(num)
            if pos == len(res):
                res.append(num)
            else:
                res[pos] = num
        return len(res)