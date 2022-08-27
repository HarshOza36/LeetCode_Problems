class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(nlogn)
#         freq = {}
#         for n in nums:
#             if n in freq:
#                 freq[n] += 1
#             else:
#                 freq[n] = 1
        
#         freq = sorted(freq, key = freq.get, reverse = True)
#         ans = []
#         for n in freq:
#             if(k == 0):
#                 break
#             ans.append(n)
#             k -= 1
#         return ans
        # we could use a heap instead of sorting to get O(n + klogn)
    
        # Bucket sort o(n)
        n = len(nums)
        # index of buckets are the frequency and the values in the index are
        # the elements having that frequency
        buckets = [[] for _ in range(n+1)]
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for ele,cnt in freq.items():
            buckets[cnt].append(ele)
        
        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for ele in buckets[i]:
                ans.append(ele)
                if len(ans) == k:
                    return ans