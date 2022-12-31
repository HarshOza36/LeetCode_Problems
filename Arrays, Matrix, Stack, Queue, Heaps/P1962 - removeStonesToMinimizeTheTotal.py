class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapify(pq)
        for i in range(k): 
            pile = heappop(pq)
            pile //= 2
            heappush(pq, pile)
        return -sum(pq)