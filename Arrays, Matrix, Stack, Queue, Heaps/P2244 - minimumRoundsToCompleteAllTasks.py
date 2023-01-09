class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = {}
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
        
        minRounds = 0
        for k,v in freq.items():
            if v == 1: return -1
            if v % 3 == 0: minRounds += v // 3
            else: 
                # if we cant divide by 3
                # then if we have remainder 1 say 7
                # XXX XXX X, we can break the last group in group of 2
                # XXX XX XX, that is 7//3 = 2 + 1 groups

                # if we have remainder 2 say 8 
                # XXX XXX XX, we will have 1 extra group of 2
                # which is 8//3 + 1 = 2 + 1
                minRounds += v // 3 + 1
        return minRounds