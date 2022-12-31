class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(nlogn) time O(n) space because python create copy of slices
        nums.sort()
        # we will sort the array
        # we will then replace even index elements with the reverse first 
        # half of this array and
        # then we will replace the odd index  elements of this array
        # with the reverse second half of this array
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
