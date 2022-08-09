class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # for n = 1, we can just have a e i o u hence 5
        # for n = 2, we can have "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua"
        
        # Now at this level we see, a is produced at E, I, U
        # e is produced at A, I
        # i is produced at E, O
        # o is produced at I
        # u is produced at I, O
        # we will store this count for each vowel
        # in such a way, we will keep count of total vowels at that level
        # by using previous count of vowels
        # Because we know that every A will be followed By E or 
        # every I wont be followed by I
        # so that next level , we know ae, here e will be followed by A, I
        a, e, i, o, u = 1, 1, 1, 1, 1
        mod = 10**9 + 7
        for _ in range(2, n + 1):
            new_a = (e + i + u) % mod
            new_e = (a + i) % mod
            new_i = (e + o) % mod
            new_o = (i) % mod
            new_u = (i + o) % mod
            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u
            
        return (a + e + i + o + u) % (mod)