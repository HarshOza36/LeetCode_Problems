class Solution:
    def originalDigits(self, s: str) -> str:
        # for 0 we just need the count of z
        # for 2 we just need count of w        
        # for 4 we just need count of u
        # for 6 we just need count of x
        # for 8 we just need count of g

        # for 1 we need count of o and we need to remove all o from 0(Z), 2(W), 4(U)
        # for 3 we need count of h and need to remove h from 8(G)
        # for 5 we need count of f and need to remove f from 4(U)
        # for 7 we need count of s and need to remove s from 6(X)
        # for 9 we need count of i and need to remove i from 5(F), 6(X) 8(G) and 4(U) since we 
        # used f from 5 and finally add the extra U from 4 to balance it out
        
        freq = collections.defaultdict(int)
        for ch in s: freq[ch] += 1
        
        ans = ""
        ans += "0" * freq['z']
        ans += "1" * (freq['o'] - freq['z'] - freq['w'] - freq['u'])
        ans += "2" * freq['w']
        ans += "3" * (freq['h'] - freq['g'])
        ans += "4" * freq['u']
        ans += "5" * (freq['f'] - freq['u'])
        ans += "6" * freq['x']
        ans += "7" * (freq['s'] - freq['x'])
        ans += "8" * freq["g"]
        ans += "9" * (freq['i'] - freq['x'] - freq["g"] - freq['f'] + freq['u'])
        return ans