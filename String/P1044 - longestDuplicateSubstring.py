from collections import defaultdict
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        out = ""
        l, r = 1, len(s) - 1
        while(l <= r): 
            mid = l + (r - l) // 2             
            dup = self.rbk(s, mid)            
            if dup: 
                l = mid + 1
                out = dup
            else: 
                r = mid - 1            
        return out


    def rbk(self, text, L):
        
        # q is the prime number
        # h is the hash
        # d is the number of characters in the input alphabet
        # t is the hash_table key
        q = (1 << 31) - 1
        
        h, t, d = (1 << (8*L-8)) % q, 0, 256
        
        hash_table = defaultdict(list)

        for i in range(L): 
            t = (d * t + ord(text[i])) % q

        hash_table[t].append(i - L + 1)

        for i in range(len(text) - L):
            t = (d* (t - ord(text[i]) * h) + ord(text[i + L])) % q

            for j in hash_table[t]:
                if(text[i+1 : i+L+1] == text[j : j+L]):
                    return text[j : j+L]
            hash_table[t].append(i+1)
        return None


obj = Solution().longestDupSubstring("banana")
print(obj)
        