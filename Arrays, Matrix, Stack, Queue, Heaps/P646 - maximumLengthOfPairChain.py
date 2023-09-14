class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        curr = float('-inf')
        ans = 0

        for start, end in pairs:
            if start > curr:
                ans += 1
                curr = end
        return ans