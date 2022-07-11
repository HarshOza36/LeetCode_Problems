class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        output = []
        l,r = 0, 1
        i = 0
        while(r < len(nums)):
            if nums[i] + 1 != naums[r]:
                if r == l+1:
                    output.append(str(nums[l]))
                else:
                    output.append(f"{nums[l]}->{nums[r-1]}")
                l = r 
                r = l + 1
                i = l
            else:
                i += 1
                r += 1
        if r == l+1:
            output.append(str(nums[l]))
        else:
            output.append(f"{nums[l]}->{nums[r-1]}")
        
        return output
            