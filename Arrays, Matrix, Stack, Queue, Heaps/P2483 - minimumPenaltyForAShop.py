class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = 0
        for c in customers:
            penalty += 1 if c == "Y" else 0
        
        minPenalty = penalty
        minPenIdx = 0

        for idx, c in enumerate(customers):
            penalty += -1 if c == 'Y' else 1
            if penalty < minPenalty:
                minPenalty = penalty
                minPenIdx = idx + 1
        return minPenIdx 