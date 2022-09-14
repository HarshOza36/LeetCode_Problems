class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        '''
        Using the example test case 3 when power >= currtoken(small power token)
        we will take it and increase score, and then decrease power with that
        currtoken. if not then we check if score is >= 1 then we take bigger 
        power token decrease score but increase power, so that
        we can then take smaller powers token we increase our score
        so we sort in ascending order and use two pointers
        '''
        score = 0
        tokens.sort()
        l,r = 0, len(tokens)-1
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif score >= 1 and l < r:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return score