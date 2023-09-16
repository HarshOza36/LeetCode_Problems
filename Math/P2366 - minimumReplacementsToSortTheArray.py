class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = nums[n - 1] 
        ans = 0  

        for i in range(n - 2, -1, -1):
            curr = nums[i]
            if curr > nxt: 
                # If the current element has to be replaced
                # We will first find the numbers we need to add, and if it doesnt totally divide
                # then we also add the remainder
                replaced = curr // nxt
                if curr % nxt: replaced += 1 
                nxt = curr // replaced 
                ans += replaced - 1 
            else:
                nxt = curr  
        return ans  