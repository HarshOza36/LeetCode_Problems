class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def dfs(idx, partition):
            if idx >= len(s):
                ans.append(partition[:])
                return

            for j in range(idx, len(s)):
                if self.isPalindrome(s, idx, j):
                    partition.append(s[idx:j+1])
                    dfs(j + 1, partition)
                    partition.pop()

        dfs(0, [])
        return ans
            
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


            

