class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        
        stamp_covers = set()
        # Building stamp permutations
        # like {'??c', 'a??', '?b?', 'abc', 'ab?', '?bc'}
        for i in range(n):
            for j in range(n-i):
                 stamp_covers.add('?' * i + stamp[i : n-j] + '?' * j)
        
        # Now we will find target substrings in stamp covers
        # if we find such, we will replace ? as values in that substring
        # finally our target string will be ? * len(target)
        final = "?" * m
        substring_len = m - n
        ans = []
        while target != final:
            
            found = False
            '''
            the below for loop will work like this
            i substring target
            2    abc    ababc
            1    b??    ab???
            0    ab?    ab???
            '''
            for i in range(substring_len, -1, -1):
                if target[i : i + n] in stamp_covers:
                    # creating the cover type
                    target = target[:i] + '?' * n + target[i + n:]  
                    ans.append(i)
                    found = True
            if not found:   
                # if we cannot find where to put the stamp, return empty array
                return []
        
        return ans[::-1]