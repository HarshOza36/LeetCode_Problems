class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # we will divide a string into
        # str = ch1 + m + ch2
        # let middle = subsequences(m) where m is mid of str
        # let count(str) = count of palindromic subsequence of str
        # subsequences(str) = count("" + middle + "") + count("" + middle + ch2)
        #                  + count(ch1 + middle + "") + count(ch1 + middle + ch2)
        #                   = a + b + c+ d ....let
        # so subsq(ch1 mid) = count(ch1 + middle) + count("" + middle) = a+c
        # # so subsq(mid ch2) = count(middle +  ch2) + count(middle + "") = b+a
        # now if ch1 == ch2
        # then in case d, it will be equal of case a plus 1
        # say case "a" middle = aba, here palindromic subs are a,b,a,aba (4)
        # if ch1 == ch2 == d, case "d" will be d, da, da, da, daba (5)

        # hence if ch1 == ch2 then subseq(Str) = a + a + b + c + 1
        #  = a+c + b+a + 1 = subseq(ch1 mid) + subset(mid ch2) + 1

        # for ch1 != ch2
        # then case"d" will be simply 0 it cannot form any palidrome
        # so subseq(str) = a + b + c
        # = a+b+c +a - a = a+c + b+a - a
        #  = subseq(ch1 mid) + subset(mid ch2) - a

                

        n = len(s)
        dp = [[0]*n for j in range(n)]
        MOD = 10**9 + 7
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i > j : continue
                elif i == j:
                    # when same they are palindrome
                    dp[i][j] = 1
                elif s[i] != s[j]:
                    # if edges not equal
                    # dp(i,j) = ch1 + ch2 - middle that is
                    # subseq(ch1 mid) + subset(mid ch2) - a
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                else:
                    # if they are same then
                    # as per the above approach we will calculate all the subseqs
                    # we need to also check duplicates and remove same subsequences
                    # so for that
                    
                    # check from start if same characters in middle
                    start = i+1
                    while start < j and s[start] != s[i]: start += 1

                    # check from end if same characters in middle
                    end = j-1
                    while end > i and s[end] != s[i]: end -= 1
                    
                    # if there are no same duplicate characters
                    # then dp(i,j) is 2 * dp(middle) + 2
                    if start == j:
                        dp[i][j] =  2 * dp[i+1][j-1] + 2
                    elif start == end:
                        # only one duplicate so we do +1 instead of + 2
                        dp[i][j] = 2 * dp[i+1][j-1] + 1
                    else:
                        # multiple duplicate so delete these by deleting 
                        # number of palidromes in middle
				        # count(ch2) - count(first last)
                        dp[i][j] = 2 * dp[i+1][j-1] - dp[start+1][end-1]
                    dp[i][j] %= MOD
        return dp[0][n-1] % MOD
