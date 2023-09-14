class Solution:
    def jump(self, nums: List[int]) -> int:
        # Basically we apply a 1d BFS and take O(n) time
        # we will start from 0 and find max jumps from the current index
        # and then we can start the window from the max jump we can take
        # so going through the nums just once and getting the minimum jumps
        # required to reach the end
        n = len(nums)
        minJumps = 0
        l = r = 0
        while(r < n-1):
            maxJumpIdx = 0
            for i in range(l, r+1):
                maxJumpIdx = max(maxJumpIdx, i + nums[i])
            l = r + 1
            r = maxJumpIdx
            minJumps += 1
        return minJumps

