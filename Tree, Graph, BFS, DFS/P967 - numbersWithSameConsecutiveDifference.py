class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def dfs(i, n, formed):
            if n == 1:
                ans.append(formed)
                return
            if i+k <= 9:
                dfs(i + k, n-1,formed*10 + (i + k))
            if i-k >= 0 and k != 0:
                dfs(i - k, n-1,formed*10 + (i - k))
    
        for i in range(1, 10):
            dfs(i, n, i)
        return ans