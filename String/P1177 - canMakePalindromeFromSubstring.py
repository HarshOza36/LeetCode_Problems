class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefixCount = [[0]*26 for _ in range(n+2)]
        # prefixCount will help us store the count of that character
        # till some index point i
        # we will have n rows, and 26 columns representing each
        # character from a-z
        
        for i in range(n):
            chrIdx = ord(s[i]) - ord('a')
            prefixCount[i+1][chrIdx] += 1
            for j in range(26):
                # from previous column add the old values to this new index
                prefixCount[i+1][j] += prefixCount[i][j]

        ans = []
        for l, r, k in queries:
            if r-l+1 <= k:
                # if the number of operaions are greater than
                # the number of characters in the window
                # we can just simply replace all characters and form 
                # palindrome
                ans.append(True)
            else:
                # Now we will check and pair up to form palindrome
                # say we have even count characters we can directly 
                # create a palindrome and if we have say one odd count
                # character we can add it to the middle of the palindrome
                # if not we cannot form a palindrome
                oddChrs = 0
                for j in range(26):
                    # count of characters in the l to r range
                    cnt = prefixCount[r+1][j] - prefixCount[l][j]
                    if cnt & 1:
                        oddChrs += 1
                
                # now once we have odd count say a,b,c,d,e are those
                # we can take k operations and replace one chr at each time
                # which helps us pair 2 chrs, removing 2 total chrs
                
                # for example if k == 2
                # we first replace d to a, which will remove a,d from list
                # then we replace e to b, which will remov b,e from list
                # keeping c finally
                # so at every operation we removed 2 chrs
                # ie. 2*k
                
                # so we will now subtract it from our oddChrs count
                oddChrs -= 2*k
                if oddChrs > 1:
                    # even after pairing if we have more than one oddChr
                    # we cannot form palindromes
                    ans.append(False)
                else:
                    ans.append(True)
        return ans
        