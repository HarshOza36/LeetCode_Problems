class Solution:
    def checkRecord(self, n: int) -> int:
        # Basically in this problem we will see how all A P L ended
        # and we take total
        # In case of P, it can be appended to all AP, PP, PL
        # so current P = prev A + prev P + prev L
        # that is P[i] = A[i-1] + P[i-1] + L[i-1]

        # For L we cannot have more than 2 L consecutively
        # If its prev character is P we make PL
        # If its prev character is A we make AL
        # If its prev character is L then we need to check prevPrev
        # prevPrev is i-2
        # so if i-2 is A we make ALL
        # so if i-2 is P we make PLL
        # we cannot make LLL if i-2 is L
        # then L[i] = A[i-1] + A[i-2] + P[i-1] + P[i-2] 
        
        # For A we cannot have more than 2 A in total
        # So if previous P and L we can make PA, LA but with a condition
        # that this Prev P and L do not have any A's previously

        # So A[i] = P_withNoA[i-1] + L_withNoA[i-1]
        # Now we need to define P_withNoA, L_withNoA

        # in P_withNoA, it is same as P but without A
        # we can add a P, if prev is P and has no A
        # we can add a P if prev is L and has no A
        # so P[i] = P[i-1] + L[i-1] and we remove A
        # P_withNoA[i] = P_withNoA[i-1] + L_withNoA[i-1]

        # Just like P_withNoA, L_withNoA is similar to L
        # L_withNoA[i] = P_withNoA[i-1] + P_withNoA[i-2]
        # since L was P[i-1] + P[i-2] and we removed A

        # Lets reduce finally to get A[i] formula
        # A[i] = P_withNoA[i-1] + L_withNoA[i-1] - 1
        # P_withNoA[i] = P_withNoA[i-1] + L_withNoA[i-1] - 2
        # So A[i] = P_withNoA[i] from 1-2
        # substitute i = i-1 and i = i-2 to get
        # A[i-1],A[i-2] = P_withNoA[i-1],P_withNoA[i-2] - 3
        # Now, 
        # A[i] = P_withNoA[i-1] + L_withNoA[i-1]
        # L_withNoA[i] = P_withNoA[i-1] + P_withNoA[i-2] - 4
        # A[i] = P_withNoA[i-1] + P_withNoA[i-2] + P_withNoA[i-3]
        # by substitute i = i-1 in L_withNoA in 4
        # A[i] = A[i-1] + A[i-2] + A[i-3] - from 3,4
        # finally with A we have 
        # P[i] = A[i-1] + P[i-1] + L[i-1]
        # L[i] = A[i-1] + A[i-2] + P[i-1] + P[i-2] 

        dp = [[None]*3 for _ in range(n+3)]

        # we do n+3 so that we adjust initializations for our 
        # equations since we look for i-3 and i-2
        # [A, L, P] is our inner array
        # Now we need to initializa as per the equations


        dp[0][0] = 1 # A[0] just A n = 1
        dp[1][0] = 2 # A[1] LA, PA n = 2
        dp[2][0] = 4 # A[2] LLA, PPA, LPA, PLA n = 3

        dp[0][1] = 1 # L[0] just L n = 1
        dp[1][1] = 3 # L[1] PL, AL, LL n = 2

        dp[0][2] = 1 # P[0] just P n = 1
        

        MOD = 10**9 + 7

        for i in range(1, n):
            #  P
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD

            if i > 1: # L
                dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][2] + dp[i-2][2]) % MOD

            if i > 2: # A
                dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD
        return sum(dp[n-1]) % MOD
