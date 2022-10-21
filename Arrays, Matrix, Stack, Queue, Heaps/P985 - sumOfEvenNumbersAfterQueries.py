class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        evenSum = 0
        for n in nums:
            if n % 2 == 0:
                evenSum += n
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                # if already even first remove the element from sum
                # it will take care, if the value gets odd after addition of
                # the query value
                evenSum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                evenSum += nums[idx] 
                
            ans.append(evenSum)
        return ans