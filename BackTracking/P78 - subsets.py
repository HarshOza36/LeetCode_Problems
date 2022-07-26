class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Runs O(N * 2^N)
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
    
    # Better method
##    def dfs(i, cur):
##            if i >= len(nums):
##                out.append(cur[:])
##                return
##
##            # Include element
##            cur.append(nums[i])
##            dfs(i + 1, cur)
##            # Exclude element
##            cur.pop()
##            dfs(i + 1, cur)
##
##    dfs(0, [])
