class Compare:
    def __init__(self, cnt, word):
        self.cnt = cnt
        self.word = word
        
    def __lt__(self, item):
        if self.cnt == item.cnt:
            return self.word > item.word
        else:
            return self.cnt < item.cnt

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # O(w + nlogn) is w=n then O(nlogn), O(n)space 97.43% faster and 94.73% less memory
#         freq = {}
#         for w in words:
#             freq[w] = 1 + freq.get(w,0)
        
#         return sorted(freq, key = lambda x : (-freq[x], x))[:k]

        # O(nlogk) as asked 
        freq = {}
        for w in words:
            freq[w] = 1 + freq.get(w,0)
        heap = []
        for key, v in freq.items():
            heapq.heappush(heap, Compare(v, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap).word for _ in range(k)][::-1]