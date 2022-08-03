class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # this is basically 2 sum
        # Add remainders we know that remainders will lie between 0 to 59
        # It is constant space O(60)
        remainders = [0] * 60
        ans = 0
        for t in time:
            rem = t % 60
            if (rem == 0):
                # if the rem is zero, then target complement will be 
                # the prev song times with remainder zero
                ans += remainders[0]
            else:
                # otherwise once we get a remainder
                # we could just check 60 - rem for complement
                # For example
                # 30, 20, 150 are seen and our
                # rem[30] = 2, rem[20] = 1
                # when we get 100, rem = 40, we can check if we had
                # 60 - 40 = 20 in our remainders array
                # because 100 + 20 will form 120 
                ans += remainders[60 - rem]
            remainders[rem] += 1

        return ans