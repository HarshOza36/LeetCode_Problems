class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        numSet = set(nums)
        currLongest = 0
        for num in numSet:
            if num-1 not in numSet:
                currLongest = 1
                currNum = num

                while currNum+1 in numSet:
                    currLongest += 1
                    currNum += 1
                    longest = max(longest, currLongest)
        return max(longest, currLongest)