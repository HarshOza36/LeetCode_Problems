class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        
        sorted_val = sorted(freq.items(), key = lambda x: (x[1],-x[0]))
        ans = []
        for num, fr in sorted_val:
            ans.extend([num]*fr)
        return ans