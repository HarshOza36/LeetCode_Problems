class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(self.nums)
        self.l = len(nums)

    def update(self, index: int, val: int) -> None:
        self.s -= self.nums[index]
        self.nums[index] = val
        self.s += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        # instead of just taking sum from l to r
        # if l to r is greater than half of the array
        # we can just take start to left sum and right to end sum
        # subtract from actual sum
        # it is faster that way
        if right - left > self.l // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.s - ans
        else:
            return sum(self.nums[left: right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)