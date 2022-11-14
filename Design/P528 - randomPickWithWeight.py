class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        # Now we will form a uniform distribution of the elements
        # so we can use the random selection
        self.prefixSum = [self.w[0]]
        for i in range(1, len(self.w)):
            self.prefixSum.append(self.prefixSum[i-1] + self.w[i])
        self.totalSum = self.prefixSum[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        pick = random.randint(1, self.totalSum)
        # once we selected a random number in the range
        # we will search the element closest to this picked random
        # number we got
        l = 0
        r = len(self.prefixSum) - 1
        while l < r:
            mid = (l + r) // 2
            if pick <= self.prefixSum[mid]:
                r = mid
            else:
                l = mid + 1
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()