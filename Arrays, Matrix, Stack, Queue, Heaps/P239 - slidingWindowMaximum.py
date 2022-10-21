class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        r = 0
        n = len(nums)
        dq = deque([])
        for r in range(n):
            # we will always keep max element as first element
            # and remove elements on left since they will be smaller 
            # than max and wont be useful
            # we need to keep the deque in decreasing order
            while dq and dq[-1] < nums[r]:
                dq.pop()
            
            dq.append(nums[r])
            
            if r-l+1 == k:
                ans.append(dq[0])
            
                if nums[l] == dq[0]:
                    dq.popleft()
            
                l += 1
            r += 1
        return ans
            