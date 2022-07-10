class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        freq = sorted(freq, key = freq.get, reverse = True)
        ans = []
        for n in freq:
            if(k == 0):
                break
            ans.append(n)
            k -= 1
        return ans
