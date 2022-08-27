class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = 1 + freq.get(num, 0)
        
        half = len(arr)//2
        
        # Sort dictionary by their frequency (descending order)
        num_freq = sorted(freq.values(), reverse=True)  
        ans = 0
        # we will remove the max frequencies first
        # directly we will subtract it from half
        # and as soon as half gets negative we return ans
        while half > 0:
            half -= num_freq[ans]
            ans += 1
        return ans