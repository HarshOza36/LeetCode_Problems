class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # O(N*K) gives TLE
        # n = len(nums)
        # for i in range(1, n):
        #     m = float("-inf")
        #     for j in range(max(i-k, 0), i):
        #         m = max(m, nums[j] + nums[i])
        #     nums[i] = m
        # return nums[n-1]
        
        # O(n) time , O(k) space
        n = len(nums)
        dq = deque([0])  
        # we store index of nums, keeping maximum one in front
        for i in range(1, n):
            # nums[i] = max of next k jump elements
            nums[i] += nums[dq[0]]

            # Add a nums[i] to the deque and element ones which are not useful
            while dq and nums[dq[-1]] <= nums[i]: 
                dq.pop()  
            dq.append(i)

            # Remove if the last element is out of window size k
            if i - dq[0] >= k: 
                dq.popleft()

        return nums[n-1]