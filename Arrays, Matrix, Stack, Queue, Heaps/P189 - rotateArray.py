class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution with extra space
        # nums[:] = nums[-(k%len(nums)):] + nums[:-(k%len(nums))]
        
        # Brute force
        # k %= len(nums)
        # # reverse full array
        # for i in range(len(nums)//2):
        #     nums[i], nums[-(i+1)] = nums[-(i+1)], nums[i]
        # # reverse till k elements
        # for i in range(k//2):
        #     nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        # # reverse from k to end
        # for i in range(k, (len(nums)-k)//2 + k):
            # nums[i], nums[len(nums)-i-1+k] = nums[len(nums)-i-1+k], nums[i]
            
        # Using 2 pointers
        k %= len(nums)
        left, diff = 0, len(nums) - k
        while(left != len(nums) - 1 and k):
            right = left + diff
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            if(left + diff > len(nums) - 1):
                new_size = (right - left) + 1
                k %= new_size
                diff -= k